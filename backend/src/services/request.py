from sqlalchemy.ext.asyncio import AsyncSession

from src.models.postgres import Request
from src.api.schemas.cooking_method import CookingMethodCreate
from src.api.schemas.cuisine import CuisineCreate
from src.api.schemas.dish_type import DishTypeCreate
from src.api.schemas.ingredient import IngredientCreate
from src.api.schemas.request import RequestCreateOut, RequestCreateIn
from src.api.schemas.user import UserGet
from src.repositories.cooking_method import CookingMethodRepository
from src.repositories.cuisine import CuisineRepository
from src.repositories.dish_type import DishTypeRepository
from src.repositories.ingredient import IngredientRepository
from src.repositories.request import RequestRepository
from src.services.BaseService import BaseService
from src.core.exceptions.handle_exceptions import handle_exceptions


class RequestService(BaseService):
    rep = RequestRepository

    @classmethod
    @handle_exceptions
    async def create(cls, session: AsyncSession, request_in: RequestCreateIn, current_user: UserGet) -> str:
        request_out = RequestCreateOut(user_id=current_user.id, **request_in.dict())
        request_id = await cls.rep.create(session, request_out)

        await session.commit()
        return request_id

    @classmethod
    @handle_exceptions
    async def delete(cls, session: AsyncSession, id_: str, is_accepted: bool) -> str:
        if is_accepted:
            request: Request = await cls.rep.get(session, id_)
            name = request.name

            if request.category_type == 'Ингредиент':
                new = IngredientCreate(name=name)
                await IngredientRepository.create(session, new)

            elif request.category_type == 'Тип блюда':
                new = DishTypeCreate(name=name)
                await DishTypeRepository.create(session, new)

            elif request.category_type == 'Кухня':
                new = CuisineCreate(name=name)
                await CuisineRepository.create(session, new)

            elif request.category_type == 'Способ приготовления':
                new = CookingMethodCreate(name=name)
                await CookingMethodRepository.create(session, new)

        item_id = await cls.rep.delete(session, id_)
        await session.commit()
        return item_id
