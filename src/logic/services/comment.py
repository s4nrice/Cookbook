from logic.repositories.comment import CommentRepository
from logic.utils.BaseService import BaseService


class CommentService(BaseService):
    rep = CommentRepository
