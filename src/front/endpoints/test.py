from datetime import date

import httpx
from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayMode, DisplayLookup
from fastui.events import GoToEvent, BackEvent
# from pydantic import BaseModel, Field
#
# from logic.models.schemas.recipe import RecipeGet
#
#
# class Recipe(BaseModel):
#     image: str
#     name: str
#     description: str
#     views: int
#
#
# front_router = APIRouter()
#
#
# async def fetch_recipes() -> list[Recipe]:
#     async with httpx.AsyncClient() as client:
#         response = await client.get("http://localhost:8080/api/v1/recipes/filter")
#         response.raise_for_status()
#         recipes = response.json()
#         return [Recipe(**recipe) for recipe in recipes]
#
