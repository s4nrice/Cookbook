from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.connection import PostgresConnection
from src.api.schemas.recipe import RecipeCreateIn, RecipeUpdateIn, RecipeFilter, RecipeGet
from src.services.recipe import RecipeService

recipe_router = APIRouter(
    prefix="/api/v1/recipes",
    tags=["Recipe"],
)


@recipe_router.post("/")
async def create_recipe(
        recipe: RecipeCreateIn = Depends(RecipeCreateIn),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    recipe_id = await RecipeService.create(session, recipe)
    return {"recipe_id": recipe_id}


@recipe_router.get("/filter", response_model=list[RecipeGet])
async def filter_recipe(
        filters: RecipeFilter = FilterDepends(RecipeFilter),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    recipes = await RecipeService.filter(session, filters)
    return recipes


@recipe_router.get("/{id_}", response_model=RecipeGet)
async def get_recipe(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    recipe = await RecipeService.get(session, id_)
    return recipe


@recipe_router.put("/")
async def update_recipe(
        recipe: RecipeUpdateIn = Depends(RecipeUpdateIn),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    recipe_id = await RecipeService.update(session, recipe)
    return {"recipe_id": recipe_id}


@recipe_router.delete("/{id_}")
async def delete_recipe(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    recipe_id = await RecipeService.delete(session, id_)
    return {"recipe_id": recipe_id}

