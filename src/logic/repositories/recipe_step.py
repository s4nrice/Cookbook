from logic.models.postgres import RecipeStep
from logic.utils.BaseRepository import BaseRepository


class RecipeStepRepository(BaseRepository):
    model = RecipeStep
