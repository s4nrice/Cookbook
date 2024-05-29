from fastapi_filter.contrib.sqlalchemy import Filter

from logic.models.postgres import CookingMethod
from logic.utils.BaseSchemas import BaseSchema, BaseModelWithValidation


class CookingMethodBase(BaseSchema):
    name: str


class CookingMethodGet(CookingMethodBase):
    id: str


class CookingMethodCreate(CookingMethodBase):
    pass


class CookingMethodUpdate(CookingMethodBase, BaseModelWithValidation):
    id: str
    name: str | None = None


class CookingMethodFilter(Filter):
    name__like: str | None = None
    name__in: list[str] | None = None
    name__nin: list[str] | None = None
    order_by: list[str] = ["name"]

    class Constants(Filter.Constants):
        model = CookingMethod
