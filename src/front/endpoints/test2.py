# import httpx
# from fastapi import FastAPI, Request, APIRouter
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from typing import List
#
# from pydantic import BaseModel
#
# # Создаем шаблонизатор Jinja2
# templates = Jinja2Templates(directory="S:\projects\PycharmProjects\diploma\src\front\endpoints\templates")
#
# # Пример данных о рецептах
# # recipes_data = [
# #     {"name": "Recipe 1", "description": "Description 1"},
# #     {"name": "Recipe 2", "description": "Description 2"},
# # ]
#
# front_router = APIRouter()
#
#
# class Recipe(BaseModel):
#     image: str
#     name: str
#     description: str
#     views: int
#
#
# async def fetch_recipes() -> list[Recipe]:
#     async with httpx.AsyncClient() as client:
#         response = await client.get("http://localhost:8080/api/v1/recipes/filter")
#         response.raise_for_status()
#         recipes = response.json()
#         return [Recipe(**recipe) for recipe in recipes]
#
#
# # Эндпоинт для отображения страницы поиска рецептов
# @front_router.get("/search", response_class=HTMLResponse)
# async def search_recipes(request: Request, query: str = None):
#     """
#     Render the search recipes page.
#     """
#
#     recipes = await fetch_recipes()
#
#     recipes = [recipe.name for recipe in recipes]
#
#     return templates.TemplateResponse("search_recipes.html", {"request": request, "recipes": recipes})
