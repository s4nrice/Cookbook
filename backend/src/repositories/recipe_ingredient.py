from src.models.postgres import RecipeIngredient

from src.repositories.BaseRepository import BaseRepository


class RecipeIngredientRepository(BaseRepository):
    model = RecipeIngredient
