from logic.models.postgres import CookingMethod

from logic.utils.BaseRepository import BaseRepository


class CookingMethodRepository(BaseRepository):
    model = CookingMethod
