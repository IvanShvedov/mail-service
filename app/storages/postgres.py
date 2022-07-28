from databases import Database

from storages.base_storage import Storage


class PostgreStorage(Storage):

    _database = None

    def __init__(
        self,
        host: str = '127.0.0.1',
        port: int = 5432,
        username: str = 'postgres',
        password: str = 'postgres',
        dbname: str = 'postgres',
        ):
        self.url =f'postgres://{username}:{password}@{host}:{port}/{dbname}'

    async def connect(self):
        self._database = Database(url = self.url)
        await self._database.connect()
    
    async def execute(self, command: str):
        res = await self._database.execute(command)
        return res

    async def fetch(self, command: str):
        res = await self._database.fetch_all(command)
        return res

    
        