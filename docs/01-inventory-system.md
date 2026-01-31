# Inventory System (CRITICAL)

## Overview
The inventory system is the CORE tension mechanism of the game. Players must make meaningful choices about what to carry, creating strategic depth and replayability.

## Design Goals
- **Meaningful choices:** Every slot matters
- **Build diversity:** Different races/jobs want different loadouts
- **Risk/reward:** Leaving items behind vs. being prepared
- **No hoarding:** Limited space forces commitment

## Slot System

### Base Inventory Size (by Race)
- **Human:** 10 slots (balanced)
- **Elf:** 8 slots (lightweight, mobile)
- **Dwarf:** 12 slots (sturdy, can carry more)
- **Golemkin:** 15 slots (massive, slow)
- **Umbral:** 9 slots (shadow beings, less physical bulk)

### Item Sizes
Items consume 1-3 slots based on type:

**1 Slot Items:**
- Daggers
- Short swords
- Light armor pieces
- Consumables (potions, food)
- Small relics
- Throwing weapons

**2 Slot Items:**
- One-handed swords
- Axes
- Hammers
- Bows
- Medium armor
- Shields
- Spell focuses
- Medium relics

**3 Slot Items:**
- Two-handed weapons (greatswords, battleaxes, heavy hammers)
- Heavy armor
- Large shields
- Massive relics

## Equipped vs. Carried
- **Equipped slots:** Items actively in use (weapon, armor, accessories)
  - Main hand (1 slot)
  - Off hand (1 slot, or empty for two-handers)
  - Armor (1 slot)
  - Accessory 1 (1 slot)
  - Accessory 2 (1 slot)
- **Carried slots:** Backup gear, consumables, quest items
- **Total = Equipped + Carried**

## Item Management
- **Pickup:** Only if inventory space available
- **Drop:** Drops item on ground (stays until leaving area)
- **Swap:** Quick-swap between carried and equipped
- **Discard:** Permanently destroys item

## Strategic Implications
- **Tank builds:** Need shields + heavy armor = less consumable space
- **Mage builds:** Staves + robes leave room for scrolls/potions
- **Hybrid builds:** Balanced gear, less room for situational tools
- **Consumable-heavy:** Light gear, stack potions/bombs/traps

## Dungeon Checkpoints
- **Rest rooms:** Between dungeon sections, can access vault storage
- **Vault storage:** Unlimited, but only accessible at checkpoints
- **Inventory swaps:** Reconfigure loadout before next section

## UI Design
- **Grid view:** Visual representation of slots
- **Weight indicator:** Show how full inventory is
- **Quick slots:** 1-4 hotkeys for fast consumable use
- **Comparison:** Hover to compare new item vs. equipped
- **Sort options:** By type, size, alphabetical

## Forbidden Mechanics
- **NO auto-pickup** (player must choose)
- **NO expanding inventory bags** (breaks core tension)
- **NO shared party inventory** (single player only)
- **NO unlimited junk storage** (vault is for meaningful swaps)

## Implementation Notes
```python
class Inventory:
    def __init__(self, max_slots):
        self.max_slots = max_slots
        self.items = []  # List of (item, slot_count) tuples
        self.equipped = {
            'main_hand': None,
            'off_hand': None,
            'armor': None,
            'accessory_1': None,
            'accessory_2': None
        }
    
    def used_slots(self):
        return sum(item.size for item in self.items)
    
    def available_slots(self):
        return self.max_slots - self.used_slots()
    
    def can_add(self, item):
        return self.available_slots() >= item.size
    
    def add_item(self, item):
        if self.can_add(item):
            self.items.append(item)
            return True
        return False
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def equip_item(self, item, slot):
        # Handle two-handed weapons
        if item.two_handed and slot == 'main_hand':
            self.equipped['off_hand'] = None
        self.equipped[slot] = item
```

## Testing Scenarios
1. Full inventory prevents pickup
2. Dropping item frees up space
3. Two-handed weapon clears off-hand
4. Race modifiers affect max slots
5. Equipment + carried ≤ max slots

---

**Status:** Design complete, ready for implementation
