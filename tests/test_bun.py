import pytest
from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun."""

    def test_get_name_returns_correct_name(self):
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"

    def test_get_price_returns_correct_price(self):
        bun = Bun("white bun", 200.5)
        assert bun.get_price() == 200.5

    def test_get_name_with_different_names(self):
        bun = Bun("red bun", 300)
        assert bun.get_name() == "red bun"

    def test_get_price_with_zero_price(self):
        bun = Bun("free bun", 0)
        assert bun.get_price() == 0
