from logic.endpoints.auth import auth_router
from logic.endpoints.comment import comment_router
from logic.endpoints.cooking_method import cooking_method_router
from logic.endpoints.cuisine import cuisine_router
from logic.endpoints.dish_type import dish_type_router
from logic.endpoints.ingredient import ingredient_router
from logic.endpoints.rating import rating_router
from logic.endpoints.recipe import recipe_router
from logic.endpoints.request import request_router
from logic.endpoints.user import user_router

from front.endpoints.test2 import front_router

routers = [
    ingredient_router,
    user_router,
    recipe_router,
    dish_type_router,
    cuisine_router,
    cooking_method_router,
    rating_router,
    comment_router,
    request_router,
    auth_router,
    front_router,
]
