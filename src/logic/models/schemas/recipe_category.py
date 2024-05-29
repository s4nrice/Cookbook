from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from logic.models.postgres import RecipeCategory
from logic.models.schemas.cooking_method import CookingMethodFilter, CookingMethodGet
from logic.models.schemas.cuisine import CuisineFilter, CuisineGet
from logic.models.schemas.dish_type import DishTypeFilter, DishTypeGet
from logic.utils.BaseSchemas import BaseSchema, BaseModelWithValidation


class RecipeCategoryBase(BaseSchema):
    pass


class RecipeCategoryGet(RecipeCategoryBase):
    id: str
    dish_type: DishTypeGet | None = None
    cuisine: CuisineGet | None = None
    cooking_method: CookingMethodGet | None = None


class RecipeCategoryCreateIn(RecipeCategoryBase, BaseModelWithValidation):
    dish_type_id: str | None = None
    cuisine_id: str | None = None
    cooking_method_id: str | None = None


class RecipeCategoryCreateOut(RecipeCategoryBase, BaseModelWithValidation):
    recipe_id: str
    dish_type_id: str | None = None
    cuisine_id: str | None = None
    cooking_method_id: str | None = None


class RecipeCategoryFilter(Filter):
    recipe_id: str | None = None
    dish_type: DishTypeFilter | None = FilterDepends(with_prefix("dish_type", DishTypeFilter))
    cuisine: CuisineFilter | None = FilterDepends(with_prefix("cuisine", CuisineFilter))
    cooking_method: CookingMethodFilter | None = FilterDepends(with_prefix("cooking_method", CookingMethodFilter))

    class Constants(Filter.Constants):
        model = RecipeCategory
