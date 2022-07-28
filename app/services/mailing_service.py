from datetime import datetime
import json
from re import A
from aiohttp import ClientSession
from dateutil import parser
import asyncio

from config import Config
from .service import Service
from entity.message import CreateMessageDTO, SendMessageDTO
from storages.base_storage import Storage
from entity.mailing import CreateMailingDTO, UpdateMailingDTO, MailingDTO
from .queries import CREATE_MAILING, DELETE_MAILING, UPDATE_MAILING, SELECT_MAILING

cfg = Config()


class MailingService:

    def __init__(self, storage: Storage):
        self.storage = storage

    async def create(self, mailing: CreateMailingDTO):
        res = await self.storage.execute(
            CREATE_MAILING.format(
                start_time=mailing.start_time,
                message=mailing.message,
                filter=mailing.filter,
                end_time=mailing.end_time
            )
        )
        return res[0]

    async def delete(self, mailing_id: str):
        await self.storage.execute(
            DELETE_MAILING.format(mailing_id=mailing_id)
        )

    async def update(self, mailing: UpdateMailingDTO):
        res = await self.storage.execute(
            UPDATE_MAILING.format(
                mailing_id=mailing.mailing_id,
                start_time=mailing.start_time,
                message=mailing.message,
                filter=mailing.filter,
                end_time=mailing.end_time
            )
        )
        return res[0]

    async def fetch(self, mailing_id: str):
        mailing = await self.storage.fetch(SELECT_MAILING.format(mailing_id=mailing_id))[0]
        res = MailingDTO(
            id=mailing[0],
            start_time=mailing[1],
            message=mailing[2],
            filter=mailing[3],
            end_time=mailing[4]
        )
        return res
    
    async def check_time(self, start_time, end_time):
        start_time = parser.parse(start_time)
        end_time = parser.parse(end_time)
        if start_time < datetime.now() and end_time > datetime.now():
            return True
        return False

    async def create_task(self, coro):
        return asyncio.get_event_loop().create_task(coro)

    async def send_message(self, mailing_id: str):
        client_service = Service().Client()
        message_service = Service().Message()
        mailing = await self.fetch(mailing_id=mailing_id)
        clients = await client_service.fetch_by_filter(filter=mailing.filter)

        check = await self.check_time(mailing.start_time, mailing.end_time)
        if not check:
            delay = parser.parse(mailing.start_time) - datetime.now()
            asyncio.sleep(delay.total_seconds())

        headers={"Authorization": "Bearer " + cfg.API_TOKEN}
        async with ClientSession(cfg.API_URL, headers=headers) as session:
            for client in clients:
                data = json.dumps(
                    SendMessageDTO(
                        id=mailing.id,
                        phone=client.phone,
                        text=mailing.message
                    )
                )
                async with session.post("/send/" + mailing.id, data=data) as resp:
                    if resp.status == 200:
                        await message_service.create(
                            CreateMessageDTO(
                                created_at=datetime.now(),
                                status="sended",
                                mailing_id=mailing.id,
                                client_id=client.id
                            )
                        )