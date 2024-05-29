from datetime import datetime

from fastapi_filter.contrib.sqlalchemy import Filter

from logic.models.postgres import Request
from logic.models.postgres.enums import CategoryEnum
from logic.utils.BaseSchemas import BaseSchema


class RequestGet(BaseSchema):
    id: str
    category_type: CategoryEnum
    name: str
    created_at: datetime
    user_id: str


class RequestCreateIn(BaseSchema):
    # category_type: CategoryEnum
    # name: str
    category_type: CategoryEnum
    name: str
    # user_id: str


class RequestCreateOut(BaseSchema):
    category_type: CategoryEnum
    name: str
    user_id: str


class RequestFilter(Filter):
    # category_type: CategoryEnum
    category_type: CategoryEnum | None = None
    # name__like: str | None = None
    user_id: str | None = None

    class Constants(Filter.Constants):
        model = Request
