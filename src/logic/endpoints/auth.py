from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from logic.authorization.auth import create_access_token, get_current_user, authenticate_user, Token, \
    ACCESS_TOKEN_EXPIRE_MINUTES, get_current_admin
from logic.models.connection import PostgresConnection
from logic.models.schemas.user import UserGet

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
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = await create_access_token(
        data={"sub": user.username, "is_admin": user.is_admin},
        expires_minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return Token(access_token=access_token, token_type="bearer")


# @auth_router.get("/userz")
# async def read_users_me(
#     current_user: Annotated[UserGet, Depends(get_current_user)],
# ):
#     return current_user


@auth_router.get("/userz")
async def read_users_me(
    current_user=Depends(get_current_user),
):
    return current_user


@auth_router.get("/admin")
async def read_admin_me(
    current_user: Annotated[UserGet, Depends(get_current_admin)],
):
    return {'response': 'hi admin'}
