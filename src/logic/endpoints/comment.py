from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from sqlalchemy.ext.asyncio import AsyncSession

from logic.models.connection import PostgresConnection
from logic.models.schemas.comment import CommentFilter, CommentCreate, CommentGet, CommentUpdate
from logic.services.comment import CommentService

comment_router = APIRouter(
    prefix="/api/v1/recipes",
    tags=["Comment"],
)
# comment_router.include_router(recipe_router)


@comment_router.post("/{recipe_id}/comments")
async def create_comment(
        comment: CommentCreate = Depends(CommentCreate),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    comment_id = await CommentService.create(session, comment)
    return {"comment_id": comment_id}


@comment_router.get("/{recipe_id}/comments/filter", response_model=list[CommentGet])
async def filter_comment(
        filters: CommentFilter = FilterDepends(CommentFilter),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    comments = await CommentService.filter(session, filters)
    return comments


@comment_router.get("/{recipe_id}/comments/{id_}", response_model=CommentGet)
async def get_comment(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    comment = await CommentService.get(session, id_)
    return comment


@comment_router.put("/{recipe_id}/comments/")
async def update_comment(
        comment: CommentUpdate = Depends(CommentUpdate),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    comment_id = await CommentService.update(session, comment)
    return {"comment_id": comment_id}


@comment_router.delete("/{recipe_id}/comments/{id_}")
async def delete_comment(
        id_: str,
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    comment_id = await CommentService.delete(session, id_)
    return {"comment_id": comment_id}

