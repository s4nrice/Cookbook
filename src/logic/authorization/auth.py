import os
from datetime import datetime, timedelta
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.exc import InvalidTokenError
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from logic.models.connection import PostgresConnection
from logic.models.schemas.user import UserGet, UserFilter
from logic.services.user import UserService

SECRET_KEY = str(os.environ.get('SECRET_KEY'))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    is_admin: bool | None = None


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")


async def get_user(session: AsyncSession, username: str) -> UserGet | None:
    # TODO mb oshibka
    user_filter = UserFilter(username=username)
    user_arr: list[UserGet] = await UserService.filter(session, user_filter)

    if len(user_arr) == 0:
        return None

    return user_arr[0]


async def authenticate_user(session: AsyncSession, username: str, password: str):
    user = await get_user(session, username)
    if not user:
        return False
    if not UserService.verify_password(password, user.password):
        return False
    return user


async def create_access_token(data: dict, expires_minutes: int = 1440):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=expires_minutes)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        is_admin: bool = payload.get("is_admin")
        if username is None or is_admin is None:
            raise credentials_exception
        token_data = TokenData(username=username, is_admin=is_admin)
    except InvalidTokenError:
        raise credentials_exception
    user = await get_user(session=session, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_admin(current_user: UserGet = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough privileges")
    return current_user
