from logging import Filter

from sqlalchemy.ext.asyncio import AsyncSession

from logic.utils.BaseSchemas import BaseSchema
from logic.utils.exceptions.handle_exceptions import handle_exceptions


class BaseService:
    rep = None

    @classmethod
    @handle_exceptions
    async def create(cls, session: AsyncSession, item: BaseSchema) -> str:
        item_id = await cls.rep.create(session, item)
        await session.commit()
        return item_id

    @classmethod
    @handle_exceptions
    async def filter(cls, session: AsyncSession, filters: Filter):
        items = await cls.rep.filter(session, filters)
        await session.commit()
        return items

    @classmethod
    @handle_exceptions
    async def get(cls, session: AsyncSession, id_: str):
        item = await cls.rep.get(session, id_)
        await session.commit()
        return item

    @classmethod
    @handle_exceptions
    async def update(cls, session: AsyncSession, item: BaseSchema) -> str:
        item_id = await cls.rep.update(session, item)
        await session.commit()
        return item_id

    @classmethod
    @handle_exceptions
    async def delete(cls, session: AsyncSession, id_: str) -> str:
        item_id = await cls.rep.delete(session, id_)
        await session.commit()
        return item_id
