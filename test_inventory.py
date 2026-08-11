import pytest

from inventory import InventoryManager


def test_add_item_increases_quantity():
    inv = InventoryManager()
    inv.add_item("widget", 10)
    assert inv.get_quantity("widget") == 10


def test_remove_item_decreases_quantity():
    inv = InventoryManager()
    inv.add_item("widget", 10)
    inv.remove_item("widget", 3)
    assert inv.get_quantity("widget") == 7


def test_remove_item_raises_when_not_enough_stock():
    inv = InventoryManager()
    inv.add_item("widget", 2)
    with pytest.raises(ValueError):
        inv.remove_item("widget", 5)


def test_get_quantity_defaults_to_zero():
    inv = InventoryManager()
    assert inv.get_quantity("nonexistent") == 0
