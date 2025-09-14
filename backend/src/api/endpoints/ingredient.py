from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.connection import PostgresConnection
from src.api.schemas.ingredient import IngredientFilter, IngredientGet, IngredientCreate, IngredientUpdate
from src.services.ingredient import IngredientService

ingredient_router = APIRouter(
    prefix="/api/v1/ingredients",
    tags=["Ingredient"],
)


@ingredient_router.post("/")
async def create_ingredient(
        ingredient: IngredientCreate = Depends(IngredientCreate),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    ingredient_id = await IngredientService.create(session, ingredient)
    return {"ingredient_id": ingredient_id}


@ingredient_router.get("/filter", response_model=list[IngredientGet])
async def filter_ingredient(
        filters: IngredientFilter = FilterDepends(IngredientFilter),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    ingredients = await IngredientService.filter(session, filters)
    return ingredients


@ingredient_router.get("/{id_}", response_model=IngredientGet)
async def get_ingredient(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    ingredient = await IngredientService.get(session, id_)
    return ingredient


@ingredient_router.put("/")
async def update_ingredient(
        ingredient: IngredientUpdate = Depends(IngredientUpdate),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    ingredient_id = await IngredientService.update(session, ingredient)
    return {"ingredient_id": ingredient_id}


@ingredient_router.delete("/{id_}")
async def delete_ingredient(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    ingredient_id = await IngredientService.delete(session, id_)
    return {"ingredient_id": ingredient_id}

