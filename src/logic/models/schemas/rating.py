from datetime import datetime

from fastapi_filter.contrib.sqlalchemy import Filter

from logic.models.postgres import Rating
from logic.models.schemas.user import UserGetPublic
from logic.utils.BaseSchemas import BaseSchema, BaseModelWithValidation


class RatingGet(BaseSchema):
    id: str
    rating: int
    created_at: datetime
    recipe_id: str
    rating_user: UserGetPublic


class RatingCreate(BaseSchema):
    rating: int
    recipe_id: str
    user_id: str


class RatingUpdate(BaseModelWithValidation):
    id: str
    rating: int | None = None


class RatingFilter(Filter):
    recipe_id: str | None = None
    user_id: str | None = None
    order_by: list[str] = ["-created_at"]

    class Constants(Filter.Constants):
        model = Rating
