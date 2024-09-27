from fastapi import HTTPException, status

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Не удалось подтвердить учетные данные",
    headers={"WWW-Authenticate": "Bearer"},
)

incorrect_creds_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неправильный логин или пароль",
    headers={"WWW-Authenticate": "Bearer"},
)
