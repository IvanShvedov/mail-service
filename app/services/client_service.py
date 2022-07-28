from time import timezone
from storages.base_storage import Storage
from .queries import CREATE_CLIENT, DELETE_CLIENT, UPDATE_CLIENT, SELECT_CLIENT_BY_FILTER
from entity.client import CreateClientDTO, UpdateClientDTO, ClientDTO


class ClientService:

    def __init__(self, storage: Storage):
        self.storage = storage

    async def create(self, client: CreateClientDTO):
        await self.storage.execute(
            CREATE_CLIENT.format(
                phone=client.phone,
                code=client.code,
                tag=client.tag,
                timezone=client.t_zone
            )
        )

    async def delete(self, client_id: str):
        await self.storage.execute(DELETE_CLIENT.format(client_id=client_id))

    async def update(self, client: UpdateClientDTO):
        await self.storage.execute(
            UPDATE_CLIENT.format(
                client_id=client.client_id,
                phone=client.phone,
                code=client.code,
                tag=client.tag,
                timezone=client.t_zone
            )
        )
    
    async def fetch_by_filter(self, filter: str):
        res = []
        clients = await self.storage.fetch(SELECT_CLIENT_BY_FILTER.format(filter=filter))
        for client in clients:
            res.append(
                ClientDTO(
                    id=client[0],
                    phone=client[1],
                    code=client[2],
                    tag=client[3],
                    t_zone=client[4]
                )
            )
        return res
