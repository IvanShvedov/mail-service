import json
from aiohttp import ClientSession
from storages.base_storage import Storage

from config import Config
from entity.message import CreateMessageDTO, UpdateMessageDTO, SendMessageDTO
from .queries import CREATE_MESSAGE, DELETE_MESSAGE, UPDATE_MESSAGE

cfg = Config()

class MessageService:

    def __init__(self, storage: Storage):
        self.storage = storage

    async def create(self, message: CreateMessageDTO):
        await self.storage.execute(
            CREATE_MESSAGE.format(
                created_at=message.created_at,
                status=message.status,
                mailing_id=message.mailing_id,
                client_id=message.client_id
            )
        )

    async def delete(self, message_id: str):
        await self.storage.execute(
            DELETE_MESSAGE.format(message_id=message_id)
        )

    async def update(self, message: UpdateMessageDTO):
        await self.storage.execute(
            UPDATE_MESSAGE.format(
                message_id=message.id,
                status=message.status
            )
        )

    async def send_message(self, message: SendMessageDTO):
        headers={"Authorization": "Bearer " + cfg.API_TOKEN}
        message = json.dumps(message.to_dict())
        async with ClientSession(cfg.API_URL, headers=headers) as session:
            async with session.post("/send/" + message.id, data=message) as resp:
                print(resp.status)