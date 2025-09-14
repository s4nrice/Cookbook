from src.models.postgres import User

from src.repositories.BaseRepository import BaseRepository


class UserRepository(BaseRepository):
    model = User
