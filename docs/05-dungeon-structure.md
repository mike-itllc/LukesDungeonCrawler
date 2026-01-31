# Dungeon Structure

## Overview
8 total dungeons, each split into 3 major sections. Each dungeon is ~1 hour of gameplay, creating an 8-10 hour game.

## Structure Formula
Each dungeon follows this pattern:
```
Hub → Dungeon Entrance
  → Section 1 (3-5 rooms)
    → Rest Room (checkpoint + inventory swap)
  → Section 2 (3-5 rooms)
    → Mid-Boss Room
    → Rest Room (checkpoint)
  → Section 3 (4-6 rooms)
    → Final Boss Room
  → Return to Hub
```

---

## Dungeon Progression

### Dungeon 1: The Stone Galleries (Tutorial)
**Theme:** Basic stone dungeon, teaches core mechanics
**Sections:**
- Section 1: Movement, basic combat, loot
- Section 2: Inventory management, mid-boss (Stone Guardian)
- Section 3: Environmental puzzles, final boss (Gallery Warden)
**Length:** ~45 minutes
**Unlocks:** Weapon upgrade shop, Dungeon 2

### Dungeon 2: The Flooded Crypts
**Theme:** Water-filled tomb, introduces environmental hazards
**Mechanics:** Water slows movement, electric enemies deal bonus damage in water
**Boss:** The Drowned King

### Dungeon 3: The Scorched Foundry
**Theme:** Fire and lava, tests armor choice
**Mechanics:** Heat damage over time, requires fire resistance or quick movement
**Boss:** Forge Colossus

### Dungeon 4: The Frozen Wastes
**Theme:** Ice and snow, tests stamina management
**Mechanics:** Cold slows stamina regen, ice floors = slippery movement
**Boss:** Frost Tyrant

### Dungeon 5: The Shadowed Archives
**Theme:** Dark library, tests vision and awareness
**Mechanics:** Limited vision, shadow enemies blend in
**Boss:** The Librarian Shade

### Dungeon 6: The Living Garden
**Theme:** Overgrown nature, tests ranged combat
**Mechanics:** Plants block paths, poison hazards, flying enemies
**Boss:** The Verdant Ancient

### Dungeon 7: The Clockwork Citadel
**Theme:** Mechanical fortress, tests timing and precision
**Mechanics:** Moving platforms, timed doors, laser grids
**Boss:** The Automaton Prime

### Dungeon 8: The Deep Vault (Final)
**Theme:** Combines all previous mechanics
**Sections:** 4 sections (longer than others)
**Boss:** The Vault Sovereign (multi-phase)

---

## Room Types

### Combat Room
- **Purpose:** Fight waves of enemies
- **Exits:** Locked until all enemies defeated
- **Loot:** Gold, consumables, occasional gear

### Puzzle Room
- **Purpose:** Solve environmental puzzle
- **Types:** Switch puzzles, block pushing, pattern matching
- **Loot:** Usually better rewards than combat

### Treasure Room
- **Purpose:** Loot chest(s)
- **Entrance:** Usually hidden or requires key
- **Contents:** Rare gear, large gold stacks, unique items

### Rest Room (Checkpoint)
- **Purpose:** Safe zone between sections
- **Features:**
  - Heal to full HP/stamina
  - Access vault storage
  - Swap inventory loadout
  - Save progress
- **No enemies:** Enemies cannot enter

### Boss Room
- **Purpose:** Major fight
- **Entry:** One-way door (cannot leave until boss defeated)
- **Loot:** Guaranteed unique drop + gold + dungeon material

### Shop Room (Hub Only)
- **Purpose:** Buy/sell items
- **Vendor:** Changes based on dungeon progress
- **Gold sink:** Weapon upgrades, consumables

---

## Dungeon Generation

### Layout Approach
**Hand-crafted rooms + procedural connections** (hybrid)
- Rooms are pre-designed for quality/balance
- Room connections are randomized for replay value
- Key path is always solvable

### Room Connection Rules
1. Must have clear entrance/exit
2. No dead-end required rooms
3. Optional rooms can be dead-ends (treasure rooms)
4. Boss rooms are always at the end
5. Rest rooms are always mid-section

---

## Progression Gates

### Keys
- **Silver Key:** Opens optional treasure rooms
- **Gold Key:** Required for mid-boss or section progression
- **Boss Key:** Required for final boss room

### Item Gates
- **Bombs:** Required to blow up cracked walls
- **Grappling Hook:** Required to cross gaps (found in Dungeon 3)
- **Lantern:** Required for dark areas (found in Dungeon 5)

---

## Difficulty Curve

### Early Dungeons (1-3)
- Forgiving combat
- Clear telegraphs
- Generous checkpoints
- Focus on teaching mechanics

### Mid Dungeons (4-6)
- Tighter combat
- Complex enemy compositions
- Longer sections between checkpoints
- Environmental hazards layer on top of combat

### Late Dungeons (7-8)
- Punishing combat
- Multi-mechanic encounters
- Resource pressure (limited healing)
- Tests all systems: inventory, job abilities, upgrades

---

## Time Budget

**Per Room:** 3-5 minutes average
- Combat room: 3-4 minutes
- Puzzle room: 4-6 minutes
- Treasure room: 1-2 minutes
- Boss fight: 5-10 minutes

**Per Section:** 15-20 minutes
**Per Dungeon:** 45-60 minutes
**Total Game:** 8-10 hours

---

## Implementation

```python
class Dungeon:
    def __init__(self, name, theme, sections):
        self.name = name
        self.theme = theme  # visual/mechanical theme
        self.sections = sections  # List of Section objects
        self.current_section = 0
    
    def load_section(self, section_num):
        return self.sections[section_num]

class Section:
    def __init__(self, rooms):
        self.rooms = rooms  # List of Room objects
        self.current_room = 0
        self.cleared = False

class Room:
    def __init__(self, room_type, enemies, loot, exits):
        self.type = room_type  # combat, puzzle, treasure, etc.
        self.enemies = enemies  # List of Enemy objects
        self.loot = loot  # List of items
        self.exits = exits  # List of door positions
        self.cleared = False
```

---

**Status:** Design complete, ready for implementation
**Dependencies:** Combat system, enemy AI, loot system
