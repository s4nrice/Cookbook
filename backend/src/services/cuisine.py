from src.repositories.cuisine import CuisineRepository
from src.services.BaseService import BaseService


class CuisineService(BaseService):
    rep = CuisineRepository
