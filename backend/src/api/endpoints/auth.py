from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.security import create_access_token, get_current_user, authenticate_user, Token, \
    ACCESS_TOKEN_EXPIRE_MINUTES, get_current_admin
from src.models.connection import PostgresConnection
from src.api.schemas.user import UserGet
from src.core.exceptions.exceptions import incorrect_creds_exception

auth_router = APIRouter(
    prefix='/api/v1',
    tags=["Authentication"],
)


@auth_router.post("/token")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: AsyncSession = Depends(PostgresConnection.get_db)
) -> Token:
    user = await authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise incorrect_creds_exception
    access_token = await create_access_token(
        data={"sub": user.username},
        expires_minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return Token(access_token=access_token, token_type="bearer")


# @auth_router.get("/userz")
# async def read_users_me(
#     current_user=Depends(get_current_user),
# ):
#     return current_user


# @auth_router.get("/admin")
# async def read_admin_me(
#     current_user: Annotated[UserGet, Depends(get_current_admin)],
# ):
#     return {'response': 'hi admin'}
