import asyncio
import uvicorn

from app.logger import create_logger
from app.constants import CONFIG_YAML_PATH
from app.app import create_app
from services.service import Service
from config import Config
from storages.postgres import PostgreStorage


config = Config(CONFIG_YAML_PATH)
logger = create_logger(config)
storage = PostgreStorage(
    host=config.DBHOST,
    port=config.DBPORT,
    dbname=config.DBNAME,
    password=config.DBPASSWORD,
    username=config.DBUSER
)
service = Service(storage)
app = create_app(config, [storage.connect])


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(storage.connect())
    uvicorn.run(app=app, host=config.HOST, port=config.PORT)