from logic.models.postgres import RecipeCategory

from logic.utils.BaseRepository import BaseRepository


class RecipeCategoryRepository(BaseRepository):
    model = RecipeCategory
