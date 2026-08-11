# inventory-manager

A simple inventory manager project.

## Usage

```python
from inventory import InventoryManager

inv = InventoryManager()
inv.add_item("widget", 10)
inv.remove_item("widget", 3)
print(inv.get_quantity("widget"))  # 7
```

## Methods

- `add_item(name, quantity=1)` — add stock for an item.
- `remove_item(name, quantity=1)` — remove stock; raises `ValueError` if there isn't enough.
- `get_quantity(name)` — get the current quantity of an item.
