from storages.base_storage import Storage
from services.client_service import ClientService


class Service:

    def __new__(cls, storage: Storage = None):
        if not hasattr(cls, '_instance'):
            cls.storage = storage
            cls._instance = super().__new__(cls)
        return cls._instance

    def Client(self):
        return ClientService(self.storage) 