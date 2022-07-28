from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse

from services.service import Service
from entity.mailing import CreateMailingDTO, UpdateMailingDTO


async def create_mailing(request: Request):
    service = Service().Mailing()
    body = await request.json()
    res = await service.create(
        CreateMailingDTO(
            start_time=body["start_time"],
            message=body["message"],
            filter=body["filter"],
            end_time=body["end_time"],
        )
    )
    
    await service.create_task()
    return JSONResponse("Mailing added", 200)


async def delete_mailing(request: Request):
    service = Service().Mailing()
    body = await request.json()
    await service.delete(mailing_id=body["mailing_id"])
    return JSONResponse("Mailing deleted", 200)


async def update_mailing(request: Request):
    service = Service().Mailing()
    body = await request.json()
    await service.update(
        UpdateMailingDTO(
            mailing_id=body["mailing_id"],
            start_time=body["start_time"],
            message=body["message"],
            filter=body["filter"],
            end_time=body["end_time"],
        )
    )
    return JSONResponse("Mailing updated", 200)


routes = [
    Route('/', create_mailing, methods=["POST"]),
    Route('/', delete_mailing, methods=['DELETE']),
    Route('/', update_mailing, methods=['PUT']),
]