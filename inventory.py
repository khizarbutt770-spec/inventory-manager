class InventoryManager:
    """Tracks item quantities in a simple in-memory inventory."""

    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity=1):
        self.items[name] = self.items.get(name, 0) + quantity

    def remove_item(self, name, quantity=1):
        if name not in self.items or self.items[name] < quantity:
            raise ValueError(f"Not enough {name} in inventory")
        self.items[name] -= quantity
        if self.items[name] == 0:
            del self.items[name]

    def get_quantity(self, name):
        return self.items.get(name, 0)
