from storages.base_storage import Storage
from entity.mailing import CreateMailingDTO, UpdateMailingDTO
from .queries import CREATE_MAILING, DELETE_MAILING, UPDATE_MAILING


class MailingService:

    def __init__(self, storage: Storage):
        self.storage = storage

    async def create(self, mailing: CreateMailingDTO):
        await self.storage.execute(
            CREATE_MAILING.format(
                start_time=mailing.start_time,
                message=mailing.message,
                filter=mailing.filter,
                end_time=mailing.end_time
            )
        )

    async def delete(self, mailing_id: str):
        await self.storage.execute(
            DELETE_MAILING.format(mailing_id=mailing_id)
        )

    async def update(self, mailing: UpdateMailingDTO):
        await self.storage.execute(
            UPDATE_MAILING.format(
                mailing_id=mailing.mailing_id,
                start_time=mailing.start_time,
                message=mailing.message,
                filter=mailing.filter,
                end_time=mailing.end_time
            )
        )