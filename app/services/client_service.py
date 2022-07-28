from storages.base_storage import Storage
from .queries import CREATE_CLIENT, DELETE_CLIENT, UPDATE_CLIENT
from entity.client import CreateClientDTO, UpdateClientDTO


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


# from datetime import datetime, timezone
# dt = datetime.now(timezone.utc)