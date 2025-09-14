from fastapi_filter.contrib.sqlalchemy import Filter

from src.models.postgres import RecipeStep
from src.api.schemas.BaseSchemas import BaseSchema


class RecipeStepBase(BaseSchema):
    step_number: int
    description: str
    image: str | None = None


class RecipeStepGet(RecipeStepBase):
    id: str


class RecipeStepCreateIn(RecipeStepBase):
    pass


class RecipeStepCreateOut(RecipeStepBase):
    recipe_id: str


class RecipeStepFilter(Filter):
    recipe_id: str | None = None
    order_by: list[str] = ['recipe_id,step_number']

    class Constants(Filter.Constants):
        model = RecipeStep
