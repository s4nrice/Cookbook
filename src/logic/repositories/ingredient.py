from logic.models.postgres import Ingredient

from logic.utils.BaseRepository import BaseRepository


class IngredientRepository(BaseRepository):
    model = Ingredient

