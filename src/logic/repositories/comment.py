from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from logic.models.postgres import Comment
from logic.utils.BaseRepository import BaseRepository


class CommentRepository(BaseRepository):
    model = Comment

    @classmethod
    async def filter(cls, session: AsyncSession, filters: Filter, sort: bool = False):
        stmt = filters.filter(
            select(cls.model)
            .options(
                joinedload(cls.model.comment_user)
            ).distinct()
        )
        stmt = filters.sort(stmt)
        res = await session.execute(stmt)
        return list(res.unique().scalars().all())

    @classmethod
    async def get(cls, session: AsyncSession, id_: str):
        stmt = (
            select(cls.model)
            .options(
                joinedload(cls.model.comment_user)
            )
            .filter(cls.model.id == id_)
            .distinct()
        )
        res = await session.execute(stmt)
        return res.scalars().first()
