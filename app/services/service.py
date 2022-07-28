from abc import ABC, abstractmethod

from storages.base_storage import Storage
from services.user_service import UserService


class AbsService(ABC):

    @abstractmethod
    def User(self):
        pass


class Service(AbsService):

    def __new__(cls, storage: Storage = None):
        if not hasattr(cls, '_instance'):
            cls.storage = storage
            cls._instance = super().__new__(cls)
        return cls._instance

    def User(self):
        return UserService(self.storage) 