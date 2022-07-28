from storages.base_storage import Storage

from entity.message import CreateMessageDTO, UpdateMessageDTO
from .queries import CREATE_MESSAGE, DELETE_MESSAGE, UPDATE_MESSAGE

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