from storages.base_storage import Storage


class UserService:

    def __init__(self, storage: Storage):
        self.storage = storage

    async def create(self):
        self.storage.execute(f"")


# from datetime import datetime, timezone
# dt = datetime.now(timezone.utc)