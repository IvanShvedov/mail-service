from typing import List

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount

from config import Config
from routes.user_routes import routes as user_routes


middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]


def configure_routes() -> List:
    routes = [
        Mount('/users', routes=user_routes)
    ]
    return routes

def create_app(cfg: Config) -> Starlette:
    app = Starlette(
        debug=cfg.DEBUG,
        routes=configure_routes(),
        middleware=middleware,
        on_startup=[]
    )
    return app