from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from logic.models.schemas.user import UserCreateIn, UserCreateOut
from logic.repositories.user import UserRepository
from logic.utils.BaseService import BaseService
from logic.utils.exceptions.handle_exceptions import handle_exceptions


class UserService(BaseService):
    rep = UserRepository
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    @handle_exceptions
    async def create(cls, session: AsyncSession, user_in: UserCreateIn) -> str:
        # hashed_password = user_in.password
        hashed_password = cls.hash_password(user_in.password)
        recipe_out = UserCreateOut(password=hashed_password, **user_in.model_dump(exclude={'password'}))
        recipe_id = await cls.rep.create(session, recipe_out)

        await session.commit()
        return recipe_id

    @classmethod
    def hash_password(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.pwd_context.verify(plain_password, hashed_password)

    # @classmethod
    # def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
    #     return plain_password == hashed_password
