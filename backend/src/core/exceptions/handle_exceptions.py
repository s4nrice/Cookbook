from functools import wraps

from fastapi import HTTPException, status
from sqlalchemy.exc import NoResultFound, IntegrityError


def handle_exceptions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)

        except IntegrityError:
            await args[1].rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Must be unique",
            )

        except NoResultFound:
            await args[1].rollback()
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Item not found',
            )

        # except Exception as e:
        #     await args[1].rollback()
        #     raise HTTPException(
        #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         detail=e.args[0]
        #     )

    return wrapper

