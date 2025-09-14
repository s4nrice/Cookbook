from src.repositories.dish_type import DishTypeRepository
from src.services.BaseService import BaseService


class DishTypeService(BaseService):
    rep = DishTypeRepository
