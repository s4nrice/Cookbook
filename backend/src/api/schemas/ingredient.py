from fastapi_filter.contrib.sqlalchemy import Filter

from src.models.postgres import Ingredient
from src.api.schemas.BaseSchemas import BaseSchema, BaseModelWithValidation


class IngredientGet(BaseSchema):
    id: str
    name: str
    proteins: float | None
    fats: float | None
    carbs: float | None


class IngredientCreate(BaseSchema):
    name: str
    proteins: float | None = None
    fats: float | None = None
    carbs: float | None = None


class IngredientUpdate(BaseModelWithValidation):
    id: str
    name: str | None = None
    proteins: float | None = None
    fats: float | None = None
    carbs: float | None = None


class IngredientFilter(Filter):
    name: str | None = None
    name__ilike: str | None = None
    # name__in: list[str] | None = None
    name__not_in: list[str] | None = None
    # order_by: list[str] = ["name"]

    class Constants(Filter.Constants):
        model = Ingredient
