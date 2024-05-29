from fastapi_filter.contrib.sqlalchemy import Filter

from logic.models.postgres import DishType
from logic.utils.BaseSchemas import BaseSchema, BaseModelWithValidation


class DishTypeBase(BaseSchema):
    name: str


class DishTypeGet(DishTypeBase):
    id: str


class DishTypeCreate(DishTypeBase):
    pass


class DishTypeUpdate(DishTypeBase, BaseModelWithValidation):
    id: str
    name: str | None = None


class DishTypeFilter(Filter):
    name__like: str | None = None
    name__in: list[str] | None = None
    name__nin: list[str] | None = None
    order_by: list[str] = ["name"]

    class Constants(Filter.Constants):
        model = DishType
