from fastapi_filter.contrib.sqlalchemy import Filter

from logic.models.postgres import Cuisine
from logic.utils.BaseSchemas import BaseSchema, BaseModelWithValidation


class CuisineBase(BaseSchema):
    name: str


class CuisineGet(CuisineBase):
    id: str


class CuisineCreate(CuisineBase):
    pass


class CuisineUpdate(CuisineBase, BaseModelWithValidation):
    id: str
    name: str | None = None


class CuisineFilter(Filter):
    name__like: str | None = None
    name__in: list[str] | None = None
    name__nin: list[str] | None = None
    order_by: list[str] = ["name"]

    class Constants(Filter.Constants):
        model = Cuisine
