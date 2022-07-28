from turtle import update
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse

from services.service import Service
from entity.client import CreateClientDTO, UpdateClientDTO


async def create_client(request: Request):
    serivce = Service().Client()
    body = await request.json()
    await serivce.create(
        CreateClientDTO(
            phone=body["phone"],
            code=body["code"],
            tag=body["tag"],
            t_zone=body["t_zone"],
        )
    )
    return JSONResponse("Client added", 200)


async def delete_client(request: Request):
    serivce = Service().Client()
    body = await request.json()
    await serivce.delete(client_id=body["client_id"])
    return JSONResponse("Client deleted", 200)


async def update_client(request: Request):
    service = Service().Client()
    body = await request.json()
    await service.update(
        UpdateClientDTO(
            client_id=body["client_id"],
            phone=body["phone"],
            code=body["code"],
            tag=body["tag"],
            t_zone=body["t_zone"],
        )
    )
    return JSONResponse("Client updated", 200)


routes = [
    Route('/', create_client, methods=["POST"]),
    Route('/', delete_client, methods=['DELETE']),
    Route('/', update_client, methods=['PUT'])
]