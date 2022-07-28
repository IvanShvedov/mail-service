from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def fetch(self, *args, **kwargs):
        pass

    @abstractmethod
    async def execute(self, *args, **kwargs):
        pass
