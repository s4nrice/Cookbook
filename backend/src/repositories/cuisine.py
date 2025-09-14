from src.models.postgres import Cuisine

from src.repositories.BaseRepository import BaseRepository


class CuisineRepository(BaseRepository):
    model = Cuisine
