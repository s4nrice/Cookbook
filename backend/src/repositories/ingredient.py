from src.models.postgres import Ingredient

from src.repositories.BaseRepository import BaseRepository


class IngredientRepository(BaseRepository):
    model = Ingredient

