from logic.models.postgres import User

from logic.utils.BaseRepository import BaseRepository


class UserRepository(BaseRepository):
    model = User
