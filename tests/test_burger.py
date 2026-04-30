import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты для класса Burger."""

    def setup_method(self):
        self.burger = Burger()
        self.bun = Bun("black bun", 100)
        self.sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        self.filling = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)


    def test_set_buns_sets_bun(self):
        self.burger.set_buns(self.bun)
        assert self.burger.bun == self.bun


    def test_add_ingredient_adds_to_list(self):
        self.burger.add_ingredient(self.sauce)
        assert self.sauce in self.burger.ingredients

    def test_add_multiple_ingredients(self):
        self.burger.add_ingredient(self.sauce)
        self.burger.add_ingredient(self.filling)
        assert len(self.burger.ingredients) == 2


    def test_remove_ingredient_removes_from_list(self):
        self.burger.add_ingredient(self.sauce)
        self.burger.remove_ingredient(0)
        assert self.sauce not in self.burger.ingredients

    def test_remove_ingredient_correct_index(self):
        self.burger.add_ingredient(self.sauce)
        self.burger.add_ingredient(self.filling)
        self.burger.remove_ingredient(0)
        assert self.burger.ingredients == [self.filling]


    def test_move_ingredient_changes_order(self):
        self.burger.add_ingredient(self.sauce)
        self.burger.add_ingredient(self.filling)
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[0] == self.filling
        assert self.burger.ingredients[1] == self.sauce

    def test_move_ingredient_back(self):
        self.burger.add_ingredient(self.sauce)
        self.burger.add_ingredient(self.filling)
        self.burger.move_ingredient(1, 0)
        assert self.burger.ingredients[0] == self.filling
        assert self.burger.ingredients[1] == self.sauce


    def test_get_price_only_bun(self):
        self.burger.set_buns(self.bun)
        assert self.burger.get_price() == 200

    def test_get_price_with_ingredients(self):
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.sauce)
        self.burger.add_ingredient(self.filling)
        assert self.burger.get_price() == 500

    def test_get_price_uses_mock_bun(self):
        mock_bun = MagicMock()
        mock_bun.get_price.return_value = 50
        self.burger.set_buns(mock_bun)
        assert self.burger.get_price() == 100


    def test_get_receipt_contains_bun_name(self):
        self.burger.set_buns(self.bun)
        receipt = self.burger.get_receipt()
        assert "black bun" in receipt

    def test_get_receipt_contains_price(self):
        self.burger.set_buns(self.bun)
        receipt = self.burger.get_receipt()
        assert "Price: 200" in receipt

    def test_get_receipt_contains_ingredient_name(self):
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.sauce)
        receipt = self.burger.get_receipt()
        assert "hot sauce" in receipt

    def test_get_receipt_contains_ingredient_type_lowercase(self):
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.sauce)
        receipt = self.burger.get_receipt()
        assert "sauce" in receipt

    def test_get_receipt_format_with_no_ingredients(self):
        self.burger.set_buns(self.bun)
        receipt = self.burger.get_receipt()
        lines = receipt.split('\n')
        assert lines[0] == '(==== black bun ====)'
        assert lines[1] == '(==== black bun ====)'

    def test_get_receipt_format_with_ingredients(self):
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.filling)
        receipt = self.burger.get_receipt()
        assert '= filling cutlet =' in receipt
