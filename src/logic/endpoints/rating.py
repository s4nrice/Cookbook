from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from sqlalchemy.ext.asyncio import AsyncSession

from logic.models.connection import PostgresConnection
from logic.models.schemas.rating import RatingFilter, RatingCreate, RatingGet, RatingUpdate
from logic.services.rating import RatingService

rating_router = APIRouter(
    prefix="/api/v1/recipes",
    tags=["Rating"],
)
# rating_router.include_router(recipe_router)


@rating_router.post("/{recipe_id}/ratings")
async def create_rating(
        rating: RatingCreate = Depends(RatingCreate),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    rating_id = await RatingService.create(session, rating)
    return {"rating_id": rating_id}


@rating_router.get("/{recipe_id}/ratings/filter", response_model=list[RatingGet])
async def filter_rating(
        filters: RatingFilter = FilterDepends(RatingFilter),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    ratings = await RatingService.filter(session, filters)
    return ratings


@rating_router.get("/{recipe_id}/ratings/{id_}", response_model=RatingGet)
async def get_rating(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    rating = await RatingService.get(session, id_)
    return rating


@rating_router.put("/{recipe_id}/ratings/")
async def update_rating(
        rating: RatingUpdate = Depends(RatingUpdate),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    rating_id = await RatingService.update(session, rating)
    return {"rating_id": rating_id}


@rating_router.delete("/{recipe_id}/ratings/{id_}")
async def delete_rating(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    rating_id = await RatingService.delete(session, id_)
    return {"rating_id": rating_id}

