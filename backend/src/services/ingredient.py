from src.repositories.ingredient import IngredientRepository
from src.services.BaseService import BaseService


class IngredientService(BaseService):
    rep = IngredientRepository
