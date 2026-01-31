# Race System

## Overview
5 playable races, each with unique stats, inventory sizes, and playstyle implications.

## Races

### Human
**Theme:** Balanced, adaptable, jack-of-all-trades

**Base Stats:**
- HP: 100
- Speed: 5.0
- Inventory Slots: 10
- Stamina: 100

**Racial Traits:**
- **Versatile:** Can equip any weapon type without penalty
- **Quick Learner:** 10% bonus gold from enemies
- **Balanced Build:** No stat penalties or bonuses

**Playstyle:** Flexible, good for new players, can pivot strategies mid-game

---

### Elf
**Theme:** Swift, magical, fragile

**Base Stats:**
- HP: 80
- Speed: 6.0
- Inventory Slots: 8
- Stamina: 120

**Racial Traits:**
- **Fleet-Footed:** +1 movement speed, faster dodge roll
- **Arcane Affinity:** Magic damage +15%
- **Lightweight:** Can only wear light armor
- **Keen Eyes:** Extended vision range in dungeons

**Playstyle:** Hit-and-run, spellcaster focus, mobility over durability

---

### Dwarf
**Theme:** Sturdy, resilient, slow

**Base Stats:**
- HP: 130
- Speed: 4.0
- Inventory Slots: 12
- Stamina: 80

**Racial Traits:**
- **Stoneborn:** +20% physical damage resistance
- **Grudgebearer:** Critical hit chance +10%
- **Heavy Haul:** Can carry heavy items without speed penalty
- **Ale-Hearted:** Potions heal 25% more

**Playstyle:** Tank, melee-focused, can afford to carry more gear

---

### Golemkin
**Theme:** Massive, slow, unkillable

**Base Stats:**
- HP: 180
- Speed: 3.5
- Inventory Slots: 15
- Stamina: 60

**Racial Traits:**
- **Stone Skin:** +30% physical damage resistance
- **Immovable:** Cannot be knocked back
- **Lumbering:** -15% movement speed
- **Crushing Blows:** Melee damage +20%
- **No Dodge:** Cannot dodge roll (too heavy)

**Playstyle:** Ultra-tank, unstoppable force, trades mobility for power

---

### Umbral
**Theme:** Shadow beings, evasive, high-risk

**Base Stats:**
- HP: 70
- Speed: 5.5
- Inventory Slots: 9
- Stamina: 110

**Racial Traits:**
- **Shadow Step:** Dodge roll has +50% i-frames
- **Nightborn:** +20% damage in dark areas
- **Fragile Form:** Takes +15% damage from all sources
- **Cursed Weapons:** Can equip dark/cursed items without penalty

**Playstyle:** Glass cannon, high skill ceiling, dodge-or-die

---

## Stat Scaling
- **HP:** Health points, determines survivability
- **Speed:** Movement speed (base 5.0 = normal)
- **Inventory Slots:** Max items you can carry
- **Stamina:** Used for dodging, blocking, special attacks

## Racial Synergies with Jobs
- **Humans:** Work well with any job (versatile)
- **Elves:** Synergize with magic jobs (Mage, Druid, Spellblade)
- **Dwarves:** Synergize with tank/melee jobs (Guardian, Berserker)
- **Golemkin:** Best as pure tanks (Juggernaut, Warden)
- **Umbral:** Best for high-mobility, risky jobs (Shadeblade, Phantom)

## Implementation
```python
class Race:
    def __init__(self, name, hp, speed, inventory_slots, stamina, traits):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.inventory_slots = inventory_slots
        self.stamina = stamina
        self.traits = traits  # List of RacialTrait objects

# Example:
RACES = {
    'human': Race('Human', hp=100, speed=5.0, inventory_slots=10, stamina=100, traits=[...]),
    'elf': Race('Elf', hp=80, speed=6.0, inventory_slots=8, stamina=120, traits=[...]),
    'dwarf': Race('Dwarf', hp=130, speed=4.0, inventory_slots=12, stamina=80, traits=[...]),
    'golemkin': Race('Golemkin', hp=180, speed=3.5, inventory_slots=15, stamina=60, traits=[...]),
    'umbral': Race('Umbral', hp=70, speed=5.5, inventory_slots=9, stamina=110, traits=[...])
}
```

---

**Status:** Design complete, ready for implementation
