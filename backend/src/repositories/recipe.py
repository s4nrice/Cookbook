from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.models.postgres import Recipe, RecipeIngredient, RecipeCategory
from src.repositories.BaseRepository import BaseRepository


class RecipeRepository(BaseRepository):
    model = Recipe

    @classmethod
    async def filter(cls, session: AsyncSession, filters: Filter, sort: bool = False):
        stmt = filters.filter(
            select(cls.model)
            .options(
                joinedload(cls.model.ingredients).joinedload(RecipeIngredient.ingredient),
                joinedload(cls.model.steps),
                joinedload(cls.model.categories)
                .options(
                    joinedload(RecipeCategory.dish_type),
                    joinedload(RecipeCategory.cuisine),
                    joinedload(RecipeCategory.cooking_method)
                ),
                joinedload(cls.model.author)
            ).distinct()
        )

        res = await session.execute(stmt)
        return list(res.unique().scalars().all())

    @classmethod
    async def get(cls, session: AsyncSession, id_: str):
        stmt = (
            select(cls.model)
            .options(
                joinedload(cls.model.ingredients).joinedload(RecipeIngredient.ingredient),
                joinedload(cls.model.steps),
                joinedload(cls.model.categories)
                .options(
                    joinedload(RecipeCategory.dish_type),
                    joinedload(RecipeCategory.cuisine),
                    joinedload(RecipeCategory.cooking_method)
                ),
                joinedload(cls.model.author)
            )
            .filter(cls.model.id == id_)
            .distinct()
        )
        res = await session.execute(stmt)
        return res.scalars().first()
