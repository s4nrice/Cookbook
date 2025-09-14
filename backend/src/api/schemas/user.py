from fastapi_filter.contrib.sqlalchemy import Filter

from src.models.postgres import User
from src.api.schemas.BaseSchemas import BaseSchema, BaseModelWithValidation


class UserPrivateBase(BaseSchema):
    username: str
    password: str
    email: str | None = None
    about_me: str | None = None
    is_profile_private: bool | None = False
    is_admin: bool | None = False
    profile_picture: str | None = None


class UserGet(UserPrivateBase):
    # id: str
    # username: str
    password: str
    is_profile_private: bool
    is_admin: bool


class UserGetPublic(BaseSchema):
    id: str
    username: str
    about_me: str | None = None
    is_profile_private: bool


class UserCreateIn(UserPrivateBase):
    # username: str
    # password: str
    # is_profile_private: bool | None = False
    # is_admin: bool | None = False
    pass

class UserCreateOut(UserPrivateBase):
    # username: str
    # password: str
    # is_profile_private: bool | None = False
    # is_admin: bool | None = False
    # profile_picture: str | None = None
    pass


class UserUpdateIn(UserPrivateBase, BaseModelWithValidation):
    id: str
    # profile_picture: str | None = None


class UserUpdateOut(UserPrivateBase, BaseModelWithValidation):
    id: str


class UserFilter(Filter):
    username: str | None = None
    is_profile_private: bool | None = None
    order_by: list[str] = ['id']

    class Constants(Filter.Constants):
        model = User
