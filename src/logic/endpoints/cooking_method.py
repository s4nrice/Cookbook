from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from sqlalchemy.ext.asyncio import AsyncSession

from logic.models.connection import PostgresConnection
from logic.models.schemas.cooking_method import CookingMethodCreate, CookingMethodUpdate, CookingMethodFilter, CookingMethodGet
from logic.services.cooking_method import CookingMethodService

cooking_method_router = APIRouter(
    prefix="/api/v1/cooking_methods",
    tags=["CookingMethod"],
)


@cooking_method_router.post("/")
async def create_cooking_method(
        cooking_method: CookingMethodCreate = Depends(CookingMethodCreate),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    cooking_method_id = await CookingMethodService.create(session, cooking_method)
    return {"cooking_method_id": cooking_method_id}


@cooking_method_router.get("/filter", response_model=list[CookingMethodGet])
async def filter_cooking_method(
        filters: CookingMethodFilter = FilterDepends(CookingMethodFilter),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    cooking_methods = await CookingMethodService.filter(session, filters)
    return cooking_methods


@cooking_method_router.get("/{id_}", response_model=CookingMethodGet)
async def get_cooking_method(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    cooking_method = await CookingMethodService.get(session, id_)
    return cooking_method


@cooking_method_router.put("/")
async def update_cooking_method(
        cooking_method: CookingMethodUpdate = Depends(CookingMethodUpdate),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    cooking_method_id = await CookingMethodService.update(session, cooking_method)
    return {"cooking_method_id": cooking_method_id}


@cooking_method_router.delete("/{id_}")
async def delete_cooking_method(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    cooking_method_id = await CookingMethodService.delete(session, id_)
    return {"cooking_method_id": cooking_method_id}

