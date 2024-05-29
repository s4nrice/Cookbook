from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from sqlalchemy.ext.asyncio import AsyncSession

from logic.models.connection import PostgresConnection
from logic.models.schemas.dish_type import DishTypeCreate, DishTypeUpdate, DishTypeFilter, DishTypeGet
from logic.services.dish_type import DishTypeService

dish_type_router = APIRouter(
    prefix="/api/v1/dish_types",
    tags=["DishType"],
)


@dish_type_router.post("/")
async def create_dish_type(
        dish_type: DishTypeCreate = Depends(DishTypeCreate),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    dish_type_id = await DishTypeService.create(session, dish_type)
    return {"dish_type_id": dish_type_id}


@dish_type_router.get("/filter", response_model=list[DishTypeGet])
async def filter_dish_type(
        filters: DishTypeFilter = FilterDepends(DishTypeFilter),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    dish_types = await DishTypeService.filter(session, filters)
    return dish_types


@dish_type_router.get("/{id_}", response_model=DishTypeGet)
async def get_dish_type(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    dish_type = await DishTypeService.get(session, id_)
    return dish_type


@dish_type_router.put("/")
async def update_dish_type(
        dish_type: DishTypeUpdate = Depends(DishTypeUpdate),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    dish_type_id = await DishTypeService.update(session, dish_type)
    return {"dish_type_id": dish_type_id}


@dish_type_router.delete("/{id_}")
async def delete_dish_type(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    dish_type_id = await DishTypeService.delete(session, id_)
    return {"dish_type_id": dish_type_id}

