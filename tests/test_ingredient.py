import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient."""

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 150.0),
        (INGREDIENT_TYPE_SAUCE, "free sauce", 0),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_get_name_returns_correct_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 150.0),
        (INGREDIENT_TYPE_SAUCE, "free sauce", 0),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_get_price_returns_correct_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    def test_get_type_returns_sauce_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_type_returns_filling_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
