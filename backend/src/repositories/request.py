from src.models.postgres import Request

from src.repositories.BaseRepository import BaseRepository


class RequestRepository(BaseRepository):
    model = Request
