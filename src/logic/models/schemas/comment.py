from datetime import datetime

from fastapi_filter.contrib.sqlalchemy import Filter

from logic.models.postgres import Comment
from logic.models.schemas.user import UserGetPublic
from logic.utils.BaseSchemas import BaseSchema, BaseModelWithValidation


class CommentGet(BaseSchema):
    id: str
    comment: str
    created_at: datetime
    recipe_id: str
    comment_user: UserGetPublic


class CommentCreate(BaseSchema):
    comment: str
    recipe_id: str
    user_id: str


class CommentUpdate(BaseModelWithValidation):
    id: str
    comment: str | None = None


class CommentFilter(Filter):
    recipe_id: str | None = None
    user_id: str | None = None
    order_by: list[str] = ["-created_at"]

    class Constants(Filter.Constants):
        model = Comment
