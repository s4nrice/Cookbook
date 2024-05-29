from logic.models.postgres import DishType

from logic.utils.BaseRepository import BaseRepository


class DishTypeRepository(BaseRepository):
    model = DishType
