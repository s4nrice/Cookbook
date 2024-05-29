from sqlalchemy.ext.asyncio import AsyncSession

from logic.models.schemas.recipe import RecipeCreateIn, RecipeCreateOut, RecipeUpdateIn, RecipeUpdateOut
from logic.models.schemas.recipe_ingredient import RecipeIngredientCreateOut, RecipeIngredientFilter
from logic.models.schemas.recipe_step import RecipeStepCreateOut, RecipeStepFilter
from logic.repositories.recipe import RecipeRepository
from logic.repositories.recipe_category import RecipeCategoryRepository
from logic.repositories.recipe_ingredient import RecipeIngredientRepository
from logic.repositories.recipe_step import RecipeStepRepository
from logic.utils.BaseService import BaseService
from logic.models.schemas.recipe_category import RecipeCategoryCreateOut, RecipeCategoryFilter
from logic.utils.exceptions.handle_exceptions import handle_exceptions


class RecipeService(BaseService):
    rep = RecipeRepository

    @classmethod
    @handle_exceptions
    async def create(cls, session: AsyncSession, recipe_in: RecipeCreateIn) -> str:
        # s3_client = YandexStorage.create_s3_client()
        # obj_name = str(uuid4())
        # s3_client.upload_fileobj(recipe_in.image, YandexStorage.bucket_name, obj_name)
        # url = f'https://{YandexStorage.bucket_name}.storage.yandexcloud.net/{obj_name}'
        #
        # recipe_out = RecipeCreateOut(image=url, **recipe_in.model_dump(exclude={'image'}))
        recipe_out = RecipeCreateOut(**recipe_in.dict())
        recipe_id = await cls.rep.create(session, recipe_out)

        for ingredient in recipe_in.ingredients:
            ingredient_create = RecipeIngredientCreateOut(recipe_id=recipe_id, **ingredient.dict())
            await RecipeIngredientRepository.create(session, ingredient_create)

        for step in recipe_in.steps:
            step_create = RecipeStepCreateOut(recipe_id=recipe_id, **step.dict())
            await RecipeStepRepository.create(session, step_create)

        for category in recipe_in.categories:
            category_create = RecipeCategoryCreateOut(recipe_id=recipe_id, **category.dict())
            await RecipeCategoryRepository.create(session, category_create)

        await session.commit()
        return recipe_id

    @classmethod
    @handle_exceptions
    async def update(cls, session: AsyncSession, recipe_in: RecipeUpdateIn) -> str:
        # TODO ДОБАВИТЬ S3
        recipe_out = RecipeUpdateOut(**recipe_in.dict())
        if len(recipe_out.model_dump(exclude={'id'}, exclude_none=True)) > 0:
            await cls.rep.update(session, recipe_out)

        if recipe_in.ingredients:
            # Удаление всех привязанных к рецепту ингредиентов
            ingredient_filter = RecipeIngredientFilter(recipe_id=recipe_in.id)
            ingredient_to_delete = await RecipeIngredientRepository.filter(session, ingredient_filter)
            ingredient_ids_to_delete = [item.id for item in ingredient_to_delete]
            [await RecipeIngredientRepository.delete(session, item) for item in ingredient_ids_to_delete]

            # Добавление новых
            for ingredient in recipe_in.ingredients:
                ingredient_create = RecipeIngredientCreateOut(recipe_id=recipe_in.id, **ingredient.dict())
                await RecipeIngredientRepository.create(session, ingredient_create)

        if recipe_in.steps:
            # Удаление всех привязанных к рецепту шагов
            step_filter = RecipeStepFilter(recipe_id=recipe_in.id)
            step_to_delete = await RecipeStepRepository.filter(session, step_filter)
            step_ids_to_delete = [item.id for item in step_to_delete]
            [await RecipeStepRepository.delete(session, item) for item in step_ids_to_delete]

            # Добавление новых
            for step in recipe_in.steps:
                step_create = RecipeStepCreateOut(recipe_id=recipe_in.id, **step.dict())
                await RecipeStepRepository.create(session, step_create)

        if recipe_in.categories:
            # Удаление всех привязанных к рецепту шагов
            category_filter = RecipeCategoryFilter(recipe_id=recipe_in.id)
            category_to_delete = await RecipeCategoryRepository.filter(session, category_filter)
            category_ids_to_delete = [item.id for item in category_to_delete]
            [await RecipeCategoryRepository.delete(session, item) for item in category_ids_to_delete]

            # Добавление новых
            for category in recipe_in.categories:
                category_create = RecipeCategoryCreateOut(recipe_id=recipe_in.id, **category.dict())
                await RecipeCategoryRepository.create(session, category_create)

        await session.commit()
        return recipe_in.id
