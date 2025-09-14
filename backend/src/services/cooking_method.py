from src.repositories.cooking_method import CookingMethodRepository
from src.services.BaseService import BaseService


class CookingMethodService(BaseService):
    rep = CookingMethodRepository
