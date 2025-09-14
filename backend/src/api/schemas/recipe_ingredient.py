from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from src.models.postgres import RecipeIngredient
from src.models.postgres.enums import MeasureType
from src.api.schemas.ingredient import IngredientFilter, IngredientGet
from src.api.schemas.BaseSchemas import BaseSchema


class RecipeIngredientBase(BaseSchema):
    quantity: int | None = None
    measure: MeasureType | None = None
    description: str | None = None


class RecipeIngredientGet(RecipeIngredientBase):
    id: str
    ingredient: IngredientGet


class RecipeIngredientCreateIn(RecipeIngredientBase):
    ingredient_id: str


class RecipeIngredientCreateOut(RecipeIngredientBase):
    recipe_id: str
    ingredient_id: str


# class RecipeIngredientUpdate(RecipeIngredientBase, BaseModelWithValidation):
#     id: str
#     ingredient_id: str | None = None


class RecipeIngredientFilter(Filter):
    recipe_id: str | None = None
    ingredient: IngredientFilter | None = FilterDepends(with_prefix("ingredient", IngredientFilter))
    # order_by: list[str] | None = ['group_name']

    class Constants(Filter.Constants):
        model = RecipeIngredient
