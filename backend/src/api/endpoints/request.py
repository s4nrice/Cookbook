from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.security import get_current_user, get_current_admin
from src.models.connection import PostgresConnection
from src.api.schemas.request import RequestFilter, RequestCreateIn, RequestGet
from src.api.schemas.user import UserGet
from src.services.request import RequestService

request_router = APIRouter(
    prefix="/api/v1/requests",
    tags=["Request"],
)


@request_router.post("/")
async def create_request(
        request: RequestCreateIn = Depends(RequestCreateIn),
        session: AsyncSession = Depends(PostgresConnection.get_db),
        current_user: UserGet = Depends(get_current_user)

):

    request_id = await RequestService.create(session, request, current_user)
    return {"request_id": request_id}


@request_router.get("/filter", response_model=list[RequestGet])
async def filter_request(
        filters: RequestFilter = FilterDepends(RequestFilter),
        session: AsyncSession = Depends(PostgresConnection.get_db),
        current_user: UserGet = Depends(get_current_admin)
):
    requests = await RequestService.filter(session, filters)
    return requests


@request_router.get("/{id_}", response_model=RequestGet)
async def get_request(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db),
        current_user: UserGet = Depends(get_current_admin)
):
    request = await RequestService.get(session, id_)
    return request


@request_router.delete("/{id_}")
async def process_request(
        id_: str,
        is_accepted: bool,
        session: AsyncSession = Depends(PostgresConnection.get_db),
        current_user: UserGet = Depends(get_current_admin)
):
    request_id = await RequestService.delete(session, id_, is_accepted)
    return {"request_id": request_id}

