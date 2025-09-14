from datetime import datetime
from typing import List
from uuid import uuid4

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

from src.models.postgres.base import Base
from src.models.postgres.enums import ComplexityType, MeasureType, CategoryEnum


# from src.schemas.ingredient import Ingredient


class User(Base):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=True, unique=True)
    about_me: Mapped[str] = mapped_column(nullable=True)
    is_profile_private: Mapped[bool] = mapped_column(nullable=False, default=False)
    is_admin: Mapped[bool] = mapped_column(nullable=False, default=False)
    # TODO ДОБАВИТЬ DEFAULT КАРТИНКУ
    profile_picture: Mapped[str] = mapped_column(nullable=True)

    # Relationships
    user_recipe: Mapped[List["Recipe"]] = relationship(back_populates="author")
    # user_rating: Mapped[List["Rating"]] = relationship(back_populates="rating_user")
    # user_comment: Mapped[List["Comment"]] = relationship(back_populates="comment_user")
    # user_request: Mapped[List["Request"]] = relationship(back_populates="request_user")
    # user_personal_category: Mapped[List["PersonalCategory"]] = relationship(back_populates="personal_category_user")
    # user_subscription_pub: Mapped[List["Subscription"]] = relationship(back_populates="subscription_pub_user")
    # user_subscription_sub: Mapped[List["Subscription"]] = relationship(back_populates="subscription_sub_user")
    # user_bookmark: Mapped[List["Bookmark"]] = relationship(back_populates="bookmark_user")


class Recipe(Base):
    __tablename__ = "recipe"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    image: Mapped[str] = mapped_column(nullable=False)
    serves: Mapped[int] = mapped_column(nullable=False)
    spent_time: Mapped[int] = mapped_column(nullable=True)
    preparation_time: Mapped[int] = mapped_column(nullable=True)
    complexity: Mapped[ComplexityType] = mapped_column(nullable=True)
    views: Mapped[int] = mapped_column(nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
    # TODO должно заполняться автоматически
    author_id: Mapped[str] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    # Dependend Relationships
    ingredients: Mapped[List["RecipeIngredient"]] = relationship(back_populates="recipe_ingredient_recipe")
    author: Mapped["User"] = relationship(back_populates="user_recipe")
    steps: Mapped[List["RecipeStep"]] = relationship(back_populates="recipe_step_recipe")
    categories: Mapped[List["RecipeCategory"]] = relationship(back_populates="recipe_category_recipe")

    # Independend Relationships
    # recipe_rating: Mapped[List["Rating"]] = relationship(back_populates="rating_recipe")
    # recipe_comment: Mapped[List["Comment"]] = relationship(back_populates="comment_recipe")
    # recipe_bookmark: Mapped[List["Bookmark"]] = relationship(back_populates="bookmark_recipe")
    # recipe_notification: Mapped[List["Notification"]] = relationship(back_populates="notification_recipe")


class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredient"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    quantity: Mapped[int] = mapped_column(nullable=True)
    measure: Mapped[MeasureType] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    # group_name: Mapped[str] = mapped_column(nullable=True)
    recipe_id: Mapped[str] = mapped_column(ForeignKey("recipe.id", ondelete="CASCADE"), nullable=False)
    ingredient_id: Mapped[str] = mapped_column(ForeignKey("ingredient.id", ondelete="RESTRICT"), nullable=False)

    # Relationships
    recipe_ingredient_recipe: Mapped["Recipe"] = relationship(back_populates="ingredients")
    ingredient: Mapped["Ingredient"] = relationship(back_populates="ingredient_recipe_ingredient", uselist=False)


class Ingredient(Base):
    __tablename__ = "ingredient"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    proteins: Mapped[float] = mapped_column(nullable=True, default=0)
    fats: Mapped[float] = mapped_column(nullable=True, default=0)
    carbs: Mapped[float] = mapped_column(nullable=True, default=0)

    # Relationships
    ingredient_recipe_ingredient: Mapped[List["RecipeIngredient"]] = relationship(back_populates="ingredient")


class DishType(Base):
    __tablename__ = "dish_type"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    # Relationships
    dish_type_recipe_category: Mapped[List["RecipeCategory"]] = relationship(
        "RecipeCategory",
        back_populates="dish_type"
    )


class Cuisine(Base):
    __tablename__ = "cuisine"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    # Relationships
    cuisine_recipe_category: Mapped[List["RecipeCategory"]] = relationship(
        "RecipeCategory",
        back_populates="cuisine"
    )


class CookingMethod(Base):
    __tablename__ = "cooking_method"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    # Relationships
    cooking_method_recipe_category: Mapped[List["RecipeCategory"]] = relationship(
        "RecipeCategory",
        back_populates="cooking_method")


class RecipeStep(Base):
    __tablename__ = "recipe_step"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    step_number: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    image: Mapped[str] = mapped_column(nullable=False)
    recipe_id: Mapped[str] = mapped_column(ForeignKey("recipe.id", ondelete="CASCADE"), nullable=False)

    # Relationships
    recipe_step_recipe: Mapped["Recipe"] = relationship(back_populates="steps")


class RecipeCategory(Base):
    __tablename__ = "recipe_category"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    recipe_id: Mapped[str] = mapped_column(ForeignKey("recipe.id", ondelete="CASCADE"), nullable=False)
    dish_type_id: Mapped[str] = mapped_column(ForeignKey("dish_type.id", ondelete="RESTRICT"), nullable=True)
    cuisine_id: Mapped[str] = mapped_column(ForeignKey("cuisine.id", ondelete="RESTRICT"), nullable=True)
    cooking_method_id: Mapped[str] = mapped_column(ForeignKey("cooking_method.id", ondelete="RESTRICT"), nullable=True)

    # Relationships
    recipe_category_recipe: Mapped["Recipe"] = relationship(back_populates="categories")

    dish_type: Mapped["DishType"] = relationship(
        "DishType",
        back_populates="dish_type_recipe_category",
        foreign_keys=[dish_type_id])
    cuisine: Mapped["Cuisine"] = relationship(
        "Cuisine",
        back_populates="cuisine_recipe_category",
        foreign_keys=[cuisine_id])
    cooking_method: Mapped["CookingMethod"] = relationship(
        "CookingMethod",
        back_populates="cooking_method_recipe_category",
        foreign_keys=[cooking_method_id])



class Request(Base):
    __tablename__ = "request"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    category_type: Mapped[CategoryEnum] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    # Relationships
    # request_user: Mapped["User"] = relationship(back_populates="user_request")


# class PersonalCategory(Base):
#     __tablename__ = "personal_category"

#     id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
#     name: Mapped[str] = mapped_column(nullable=False)
#     user_id: Mapped[str] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

#     # Relationships
#     # personal_category_user: Mapped["User"] = relationship(back_populates="user_personal_category")
#     # personal_category_bookmark: Mapped[List["Bookmark"]] = relationship(back_populates="bookmark_personal_category")


class Bookmark(Base):
    __tablename__ = "bookmark"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
    recipe_id: Mapped[str] = mapped_column(ForeignKey("recipe.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    # personal_category_id: Mapped[str] = mapped_column(ForeignKey("personal_category.id", ondelete="SET NULL"), nullable=True)

    # Relationships
    # bookmark_user: Mapped["User"] = relationship(back_populates="user_bookmark")
    # bookmark_recipe: Mapped["Recipe"] = relationship(back_populates="recipe_bookmark")
    # bookmark_personal_category: Mapped[List["PersonalCategory"]] = relationship(back_populates="personal_category_bookmark")
