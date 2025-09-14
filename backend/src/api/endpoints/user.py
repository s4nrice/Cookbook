from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.connection import PostgresConnection
from src.api.schemas.user import UserFilter, UserCreateIn, UserGet, UserUpdateIn
from src.services.user import UserService

user_router = APIRouter(
    prefix="/api/v1/users",
    tags=["User"],
)


@user_router.post("/")
async def create_user(
        user: UserCreateIn = Depends(UserCreateIn),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    user_id = await UserService.create(session, user)
    return {"user_id": user_id}


@user_router.get("/filter", response_model=list[UserGet])
async def filter_user(
        filters: UserFilter = FilterDepends(UserFilter),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    users = await UserService.filter(session, filters)
    return users


@user_router.get("/{id_}", response_model=UserGet)
async def get_user(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    user = await UserService.get(session, id_)
    return user


@user_router.put("/")
async def update_user(
        user: UserUpdateIn = Depends(UserUpdateIn),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    user_id = await UserService.update(session, user)
    return {"user_id": user_id}


@user_router.delete("/{id_}")
async def delete_user(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    user_id = await UserService.delete(session, id_)
    return {"user_id": user_id}

