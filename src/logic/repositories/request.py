from logic.models.postgres import Request

from logic.utils.BaseRepository import BaseRepository


class RequestRepository(BaseRepository):
    model = Request
