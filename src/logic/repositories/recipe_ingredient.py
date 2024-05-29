from logic.models.postgres import RecipeIngredient

from logic.utils.BaseRepository import BaseRepository


class RecipeIngredientRepository(BaseRepository):
    model = RecipeIngredient
