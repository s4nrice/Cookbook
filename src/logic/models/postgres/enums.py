from enum import StrEnum


class ComplexityType(StrEnum):

    low = "Низкая"
    middle = "Средняя"
    high = "Высокая"


class CategoryEnum(StrEnum):

    ingredient = "Ингредиент"
    dish_type = "Тип блюда"
    cuisine = "Кухня"
    cooking_method = "Способ приготовления"


class MeasureType(StrEnum):

    to_taste = "по вкусу"
    pieces = "шт."
    grams = "г."
    kilogram = "кг."
    milliliters = "мл."
    liters = "л."
    glass = "стак."
    teaspoon = "ч.л."
    tablespoon = "ст.л."
    pack = "упак."
    pinch = "щеп."
    clove = "зубч."
    slice = "ломт."

