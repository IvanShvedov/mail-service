from datetime import datetime
from email.mime import base
import json
from aiohttp import ClientSession
from dateutil import parser
import asyncio
from typing import List

from config import Config


from .message_service import MessageService
from entity.client import ClientDTO
from entity.message import CreateMessageDTO, SendMessageDTO
from storages.base_storage import Storage
from entity.mailing import CreateMailingDTO, UpdateMailingDTO, MailingDTO
from .queries import CREATE_MAILING, DELETE_MAILING, UPDATE_MAILING, SELECT_MAILING


class MailingService:


    def __init__(self, storage: Storage, cfg: Config):
        self.storage = storage
        self.cfg = cfg


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
        mailing = await self.storage.fetch(SELECT_MAILING.format(mailing_id=mailing_id))
        mailing = mailing[0]
        res = MailingDTO(
            id=mailing[0],
            start_time=mailing[1],
            message=mailing[2],
            filter=mailing[3],
            end_time=mailing[4]
        )
        return res
    

    async def check_time(self, start_time, end_time):
        if start_time < datetime.now() and end_time > datetime.now():
            return True
        return False


    async def create_task(self, coro):
        return asyncio.get_event_loop().create_task(coro)


    async def send_message(self, mailing: MailingDTO, clients: List[ClientDTO]):
        check = await self.check_time(mailing.start_time, mailing.end_time)
        if not check:
            delay = mailing.start_time - datetime.now()
            await asyncio.sleep(delay.total_seconds())

        message_service = MessageService(self.storage)
        headers={"Authorization": "Bearer " + self.cfg.API_TOKEN}
        async with ClientSession(headers=headers) as session:
            for client in clients:
                data = json.dumps(
                    SendMessageDTO(
                        id=mailing.id,
                        phone=client.code + client.phone,
                        text=mailing.message
                    ).to_dict()
                )
                async with session.post(self.cfg.API_URL + str(mailing.id), data=data, ssl=False) as resp:
                    if resp.status == 200:
                        await message_service.create(
                            CreateMessageDTO(
                                created_at=datetime.now(),
                                status="sended",
                                mailing_id=mailing.id,
                                client_id=client.id
                            )
                        )