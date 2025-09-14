from src.models.postgres import CookingMethod

from src.repositories.BaseRepository import BaseRepository


class CookingMethodRepository(BaseRepository):
    model = CookingMethod
