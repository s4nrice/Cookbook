from src.models.postgres import DishType

from src.repositories.BaseRepository import BaseRepository


class DishTypeRepository(BaseRepository):
    model = DishType
