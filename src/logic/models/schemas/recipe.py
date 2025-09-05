from datetime import datetime

from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from logic.models.postgres import Recipe
from logic.models.postgres.enums import ComplexityType
from logic.models.schemas.recipe_category import RecipeCategoryGet, RecipeCategoryCreateIn, RecipeCategoryFilter
from logic.models.schemas.recipe_ingredient import RecipeIngredientFilter, RecipeIngredientGet, RecipeIngredientCreateIn
from logic.models.schemas.recipe_step import RecipeStepGet, RecipeStepFilter, RecipeStepCreateIn
from logic.models.schemas.user import UserGetPublic
from logic.utils.BaseSchemas import BaseSchema, BaseModelWithValidation


class RecipeBase(BaseSchema):
    name: str | None = None
    description: str | None = None
    serves: int | None = None
    spent_time: int | None = None
    preparation_time: int | None = None
    complexity: ComplexityType | None = None


class RecipeGet(RecipeBase):
    id: str
    name: str
    image: str | None
    serves: int
    created_at: datetime
    views: int | None
    ingredients: list[RecipeIngredientGet]
    steps: list[RecipeStepGet]
    categories: list[RecipeCategoryGet]
    author: UserGetPublic


class RecipeCreateIn(RecipeBase):
    # TODO type FILE vvv
    name: str
    image: str | None = None
    serves: int
    author_id: str
    ingredients: list[RecipeIngredientCreateIn] | None = []
    steps: list[RecipeStepCreateIn] | None = []
    categories: list[RecipeCategoryCreateIn] | None = []


class RecipeCreateOut(RecipeBase):
    name: str
    image: str
    serves: int
    # TODO должно заполняться автоматически
    author_id: str


class RecipeUpdateIn(RecipeBase, BaseModelWithValidation):
    id: str
    # TODO type FILE vvv
    image: str | None = None
    views: int | None = None
    ingredients: list[RecipeIngredientCreateIn] | None = None
    steps: list[RecipeStepCreateIn] | None = None
    categories: list[RecipeCategoryCreateIn] | None = None


class RecipeUpdateOut(RecipeBase):
    id: str
    image: str | None = None
    views: int | None = None


class RecipeFilter(Filter):
    name: str | None = None
    spent_time: int | None = None
    complexity: ComplexityType | None = None
    author_id: str | None = None
    recipe_ingredient: RecipeIngredientFilter | None = FilterDepends(with_prefix("recipe_ingredient", RecipeIngredientFilter))
    steps: RecipeStepFilter | None = FilterDepends(with_prefix("step", RecipeStepFilter))
    categories: RecipeCategoryFilter | None = FilterDepends(with_prefix("categories", RecipeCategoryFilter))

    # can sort by "views,created_at,rating.rating"
    order_by: list[str] = ['-views']

    class Constants(Filter.Constants):
        model = Recipe
