from storages.base_storage import Storage
from services.message_service import MessageService
from services.client_service import ClientService
from services.mailing_service import MailingService


class Service:

    def __new__(cls, storage: Storage = None):
        if not hasattr(cls, '_instance'):
            cls.storage = storage
            cls._instance = super().__new__(cls)
        return cls._instance

    def Client(self):
        return ClientService(self.storage)

    def Mailing(self):
        return MailingService(self.storage)

    def Message(self):
        return MessageService(self.storage)