from fastapi_filter.contrib.sqlalchemy import Filter

from logic.models.postgres import User
from logic.utils.BaseSchemas import BaseSchema, BaseModelWithValidation


class UserPrivateBase(BaseSchema):
    username: str | None = None
    password: str | None = None
    email: str | None = None
    about_me: str | None = None
    is_profile_private: bool | None = None
    is_admin: bool | None = None
    profile_picture: str | None = None


class UserGet(UserPrivateBase):
    id: str
    username: str
    password: str
    is_profile_private: bool
    is_admin: bool


class UserGetPublic(BaseSchema):
    id: str
    username: str
    about_me: str | None = None
    is_profile_private: bool
    # TODO s3 + изменить на обязательный
    profile_picture: str | None = None


class UserCreateIn(UserPrivateBase):
    username: str
    password: str
    is_profile_private: bool | None = False
    is_admin: bool | None = False
    # TODO S3
    profile_picture: str | None = None


class UserCreateOut(UserPrivateBase):
    username: str
    password: str
    is_profile_private: bool | None = False
    is_admin: bool | None = False
    profile_picture: str | None = None


class UserUpdateIn(UserPrivateBase, BaseModelWithValidation):
    id: str
    # TODO S3
    profile_picture: str | None = None


class UserUpdateOut(UserPrivateBase, BaseModelWithValidation):
    id: str


class UserFilter(Filter):
    username: str | None = None
    is_profile_private: bool | None = None
    order_by: list[str] = ['id']

    class Constants(Filter.Constants):
        model = User
