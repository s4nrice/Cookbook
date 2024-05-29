# from fastapi import FastAPI, HTTPException, Query, APIRouter
# from fastapi.responses import HTMLResponse
# from fastui import FastUI, AnyComponent, prebuilt_html, components as c
# from fastui.components.display import DisplayMode, DisplayLookup
# from pydantic import BaseModel
# from typing import List
#
# from logic.models.schemas.recipe import RecipeGet
#
# front_router = APIRouter()
#
#
# @front_router.get("/api/", response_model=FastUI, response_model_exclude_none=True)
# def recipe_list(recipes: list[RecipeGet]) -> List[AnyComponent]:
#     # recipe_components = []
#     #
#     # for recipe in recipes:
#     #     recipe_components.append(
#     #         c.Column(
#     #             components=[
#     #                 c.Image(src=recipe.image),
#     #                 c.Text(text=recipe.name, size=20, bold=True),
#     #                 c.Text(text=recipe.description),
#     #                 c.Text(text=f"Просмотры: {recipe.views}"),
#     #                 c.Text(text=f"Средняя оценка: {4.5}"),  # Замените на реальную среднюю оценку
#     #                 c.Button(text="Добавить в избранное")
#     #             ]
#     #         )
#     #     )
#
#     return [
#         c.Page(
#             components=[
#                 c.Heading(text="Рецепты", level=2),
#                 c.Form(
#                     components=[
#                         c.FormFieldInput(name="query", placeholder="Поиск"),
#                         c.Button(text="Искать")
#                     ],
#                 ),
#                 # c.Table(
#                 #     data=recipe_display_data,
#                 #     columns=[
#                 #         c.DisplayLookup(field="image", title="Изображение"),
#                 #         c.DisplayLookup(field="name", title="Название"),
#                 #         c.DisplayLookup(field="description", title="Описание"),
#                 #         c.DisplayLookup(field="views", title="Просмотры"),
#                 #         c.DisplayLookup(field="rating", title="Средняя оценка")
#                 #     ],
#                 #     no_data_message="Рецепты не найдены."
#                 # )
#             ]
#         ),
#     ]
#
#
# # @front_router.get("/api/recipe/{recipe_id}/", response_model=FastUI, response_model_exclude_none=True)
# # def recipe_detail(recipe_id: str) -> List[AnyComponent]:
# #     try:
# #         recipe = next(r for r in recipes if r.id == recipe_id)
# #     except StopIteration:
# #         raise HTTPException(status_code=404, detail="Recipe not found")
# #     return [
# #         c.Page(
# #             components=[
# #                 c.Heading(text=recipe.name, level=2),
# #                 c.Image(src=recipe.image),
# #                 c.Text(text=recipe.description),
# #                 c.Text(text=f"Просмотры: {recipe.views}"),
# #                 c.Text(text=f"Средняя оценка: {4.5}"),  # Замените на реальную среднюю оценку
# #                 c.Link(components=[c.Text(text="Назад")], on_click=c.BackEvent()),
# #                 c.Details(data=recipe)
# #             ]
# #         ),
# #     ]
#
#
# # @front_router.get("/{path:path}")
# @front_router.get("/{path:path}")
# async def html_landing() -> HTMLResponse:
#     return HTMLResponse(prebuilt_html(title="FastUI Recipes"))
