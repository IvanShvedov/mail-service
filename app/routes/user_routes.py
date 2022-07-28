from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse

from services.service import Service

async def create_user(request: Request):
    s = Service().User()
    return JSONResponse("test")



routes = [
    Route('/', create_user, methods=["POST"])
]