from src.api.endpoints.auth import auth_router
from src.api.endpoints.cooking_method import cooking_method_router
from src.api.endpoints.cuisine import cuisine_router
from src.api.endpoints.dish_type import dish_type_router
from src.api.endpoints.ingredient import ingredient_router
from src.api.endpoints.recipe import recipe_router
from src.api.endpoints.request import request_router
from src.api.endpoints.user import user_router


routers = [
    ingredient_router,
    user_router,
    recipe_router,
    dish_type_router,
    cuisine_router,
    cooking_method_router,
    request_router,
    auth_router,
]
