import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database."""

    def setup_method(self):
        self.db = Database()

    # --- available_buns ---

    def test_available_buns_returns_list(self):
        buns = self.db.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_not_empty(self):
        buns = self.db.available_buns()
        assert len(buns) > 0

    def test_available_buns_returns_bun_instances(self):
        buns = self.db.available_buns()
        for bun in buns:
            assert isinstance(bun, Bun)

    def test_available_buns_count(self):
        buns = self.db.available_buns()
        assert len(buns) == 3

    def test_available_buns_contains_black_bun(self):
        names = [b.get_name() for b in self.db.available_buns()]
        assert "black bun" in names

    def test_available_buns_contains_white_bun(self):
        names = [b.get_name() for b in self.db.available_buns()]
        assert "white bun" in names

    def test_available_buns_contains_red_bun(self):
        names = [b.get_name() for b in self.db.available_buns()]
        assert "red bun" in names

    # --- available_ingredients ---

    def test_available_ingredients_returns_list(self):
        ingredients = self.db.available_ingredients()
        assert isinstance(ingredients, list)

    def test_available_ingredients_not_empty(self):
        ingredients = self.db.available_ingredients()
        assert len(ingredients) > 0

    def test_available_ingredients_returns_ingredient_instances(self):
        ingredients = self.db.available_ingredients()
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)

    def test_available_ingredients_count(self):
        ingredients = self.db.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_contains_sauces(self):
        types = [i.get_type() for i in self.db.available_ingredients()]
        assert INGREDIENT_TYPE_SAUCE in types

    def test_available_ingredients_contains_fillings(self):
        types = [i.get_type() for i in self.db.available_ingredients()]
        assert INGREDIENT_TYPE_FILLING in types

    def test_available_ingredients_contains_hot_sauce(self):
        names = [i.get_name() for i in self.db.available_ingredients()]
        assert "hot sauce" in names

    def test_available_ingredients_contains_cutlet(self):
        names = [i.get_name() for i in self.db.available_ingredients()]
        assert "cutlet" in names
