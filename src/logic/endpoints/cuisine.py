from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from sqlalchemy.ext.asyncio import AsyncSession

from logic.models.connection import PostgresConnection
from logic.models.schemas.cuisine import CuisineCreate, CuisineUpdate, CuisineFilter, CuisineGet
from logic.services.cuisine import CuisineService

cuisine_router = APIRouter(
    prefix="/api/v1/cuisines",
    tags=["Cuisine"],
)


@cuisine_router.post("/")
async def create_cuisine(
        cuisine: CuisineCreate = Depends(CuisineCreate),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    cuisine_id = await CuisineService.create(session, cuisine)
    return {"cuisine_id": cuisine_id}


@cuisine_router.get("/filter", response_model=list[CuisineGet])
async def filter_cuisine(
        filters: CuisineFilter = FilterDepends(CuisineFilter),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    cuisines = await CuisineService.filter(session, filters)
    return cuisines


@cuisine_router.get("/{id_}", response_model=CuisineGet)
async def get_cuisine(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    cuisine = await CuisineService.get(session, id_)
    return cuisine


@cuisine_router.put("/")
async def update_cuisine(
        cuisine: CuisineUpdate = Depends(CuisineUpdate),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    cuisine_id = await CuisineService.update(session, cuisine)
    return {"cuisine_id": cuisine_id}


@cuisine_router.delete("/{id_}")
async def delete_cuisine(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    cuisine_id = await CuisineService.delete(session, id_)
    return {"cuisine_id": cuisine_id}

