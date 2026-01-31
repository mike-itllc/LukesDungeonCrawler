"""
Inventory system implementation
"""

class Item:
    """Base item class"""
    def __init__(self, name, size, item_type):
        self.name = name
        self.size = size  # Number of slots (1-3)
        self.item_type = item_type  # weapon, armor, consumable, etc.
        self.description = ""
    
    def __repr__(self):
        return f"{self.name} ({self.size} slot{'s' if self.size > 1 else ''})"

class Inventory:
    """Slot-based inventory system"""
    def __init__(self, max_slots):
        self.max_slots = max_slots
        self.items = []  # List of Item objects
        
        # Equipped slots
        self.equipped = {
            'main_hand': None,
            'off_hand': None,
            'armor': None,
            'accessory_1': None,
            'accessory_2': None
        }
    
    def used_slots(self):
        """Calculate total slots used"""
        return sum(item.size for item in self.items)
    
    def available_slots(self):
        """Calculate available slots"""
        return self.max_slots - self.used_slots()
    
    def can_add(self, item):
        """Check if item can be added"""
        return self.available_slots() >= item.size
    
    def add_item(self, item):
        """Add item to inventory"""
        if self.can_add(item):
            self.items.append(item)
            return True
        return False
    
    def remove_item(self, item):
        """Remove item from inventory"""
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def equip_item(self, item, slot):
        """Equip item to a slot"""
        # TODO: Add validation for item type vs slot
        # TODO: Handle two-handed weapons
        self.equipped[slot] = item
    
    def unequip_item(self, slot):
        """Unequip item from a slot"""
        self.equipped[slot] = None
    
    def get_equipped_item(self, slot):
        """Get currently equipped item in slot"""
        return self.equipped.get(slot)

# Example items for testing
class Sword(Item):
    def __init__(self):
        super().__init__("Iron Sword", size=2, item_type="weapon")
        self.description = "A basic one-handed sword"

class Potion(Item):
    def __init__(self):
        super().__init__("Health Potion", size=1, item_type="consumable")
        self.description = "Restores 50 HP"

class Greatsword(Item):
    def __init__(self):
        super().__init__("Greatsword", size=3, item_type="weapon")
        self.description = "A massive two-handed sword"
