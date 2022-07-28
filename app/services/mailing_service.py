from datetime import datetime
from dateutil import parser

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
    
    async def check_time(self, start_time, end_time):
        start_time = parser.parse(start_time)
        end_time = parser.parse(end_time)
        if start_time < datetime.now() and end_time > datetime.now():
            return True
        return False
