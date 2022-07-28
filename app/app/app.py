from typing import List

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount

from config import Config
from routes.client_routes import routes as client_routes
from routes.mailing_routes import routes as mailing_routes



middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]


def configure_routes() -> List:
    routes = [
        Mount('/clients', routes=client_routes),
        Mount('/mailing', routes=mailing_routes),
    ]
    return routes

def create_app(cfg: Config, on_startup=[]) -> Starlette:
    app = Starlette(
        debug=cfg.DEBUG,
        routes=configure_routes(),
        middleware=middleware,
        on_startup=on_startup
    )
    return app