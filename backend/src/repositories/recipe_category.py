from src.models.postgres import RecipeCategory

from src.repositories.BaseRepository import BaseRepository


class RecipeCategoryRepository(BaseRepository):
    model = RecipeCategory
