from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.BaseSchemas import BaseSchema


class BaseRepository:
    model = None
    
    @classmethod
    async def create(cls, session: AsyncSession, item: BaseSchema) -> str:
        query_params = item.model_dump(exclude_none=True)
        stmt = insert(cls.model).values(**query_params).returning(cls.model.id)
        res = await session.execute(stmt)
        return res.scalar_one()

    @classmethod
    async def filter(cls, session: AsyncSession, filters: Filter, sort: bool = False) -> list[model]:
        stmt = filters.filter(select(cls.model))
        if sort:
            stmt = filters.sort(stmt)
        res = await session.execute(stmt)
        return list(res.scalars().all())

    @classmethod
    async def get(cls, session: AsyncSession, id_: str) -> model:
        stmt = select(cls.model).where(cls.model.id == id_)
        res = await session.execute(stmt)
        res = res.scalar_one()
        return res

    @classmethod
    async def update(cls, session: AsyncSession, item: BaseSchema) -> str:
        id_ = str(item.id)
        query_params = item.model_dump(exclude={"id"}, exclude_none=True)

        stmt = update(cls.model).where(cls.model.id == id_).values(**query_params).returning(cls.model.id)
        res = await session.execute(stmt)
        return res.scalar_one()

    @classmethod
    async def delete(cls, session: AsyncSession, id_: str) -> str:
        stmt = delete(cls.model).where(cls.model.id == id_).returning(cls.model.id)
        res = await session.execute(stmt)
        return res.scalar_one()


