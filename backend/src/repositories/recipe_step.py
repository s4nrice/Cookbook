from src.models.postgres import RecipeStep
from src.repositories.BaseRepository import BaseRepository


class RecipeStepRepository(BaseRepository):
    model = RecipeStep
