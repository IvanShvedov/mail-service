from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse

from services.service import Service
from entity.mailing import CreateMailingDTO, UpdateMailingDTO


async def create_mailing(request: Request):
    mailing_service = Service().Mailing()
    client_service = Service().Client()
    body = await request.json()
    mailing_id = await mailing_service.create(
        CreateMailingDTO(
            start_time=body["start_time"],
            message=body["message"],
            filter=body["filter"],
            end_time=body["end_time"],
        )
    )
    mailing = await mailing_service.fetch(mailing_id=mailing_id)
    clients = await client_service.fetch_by_filter(filter=mailing.filter)
    await mailing_service.create_task(mailing_service.send_message(mailing=mailing, clients=clients))
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