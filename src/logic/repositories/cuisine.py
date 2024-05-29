from logic.models.postgres import Cuisine

from logic.utils.BaseRepository import BaseRepository


class CuisineRepository(BaseRepository):
    model = Cuisine
