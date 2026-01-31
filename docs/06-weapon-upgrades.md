# Weapon Upgrade System

## Overview
Branching upgrade paths that lock players into specific playstyles. Upgrades cost gold + dungeon materials. Once chosen, upgrades are permanent (cannot respec).

## Design Goals
- **Meaningful choices:** Each upgrade path feels distinct
- **Build commitment:** Cannot have everything, must specialize
- **Resource sink:** Gold + materials create progression economy

---

## Upgrade Structure

### Tier System
Each weapon has 3 tiers of upgrades:
- **Tier 1:** Minor stat boost, unlocks path choice
- **Tier 2:** Choose path A or B (LOCKED IN)
- **Tier 3:** Final upgrade for chosen path

### Example: Iron Sword
**Base:** 10 damage, 1.0 attack speed

**Tier 1 Upgrade** (100 gold + 5 stone)
→ 12 damage, 1.0 attack speed

**Tier 2 Choice:**
- **Path A: Heavy Blade** (300 gold + 10 iron)
  → 18 damage, 0.8 attack speed (slower, heavier hits)
- **Path B: Swift Blade** (300 gold + 10 iron)
  → 14 damage, 1.3 attack speed (faster, lighter hits)

**Tier 3:**
- **Path A → Cleaving Blade** (500 gold + boss material)
  → 25 damage, 0.7 speed, cleave hits multiple enemies
- **Path B → Rapier** (500 gold + boss material)
  → 18 damage, 1.5 speed, +20% crit chance

---

## Materials

### Common Materials (from enemies)
- **Stone Shards:** Dungeon 1-2 enemies
- **Iron Scraps:** Dungeon 3-4 enemies  
- **Frost Crystals:** Dungeon 4 enemies
- **Shadow Essence:** Dungeon 5-6 enemies

### Rare Materials (from bosses)
- **Guardian Core:** Dungeon 1 boss
- **Drowned Heart:** Dungeon 2 boss
- **Forge Ember:** Dungeon 3 boss
- (etc. one per dungeon boss)

---

## Upgrade Paths by Weapon Type

### Melee Weapons
- **Power path:** More damage, slower
- **Speed path:** Less damage, faster
- **Hybrid path:** Balanced with unique effect

### Ranged Weapons
- **Precision path:** More damage, longer charge
- **Rapid path:** Less damage, no charge time
- **Multi-shot path:** Multiple projectiles, lower accuracy

### Magic Staves
- **Destruction path:** Pure damage increase
- **Control path:** Add crowd control (slow, stun)
- **Utility path:** Lower damage, add buffs/healing

---

## Gold Costs
- **Tier 1:** 100-200 gold
- **Tier 2:** 300-500 gold
- **Tier 3:** 500-800 gold
- **Total per weapon:** 900-1500 gold

**Gold sources:**
- Enemies: 5-20 gold each
- Chests: 50-100 gold
- Bosses: 200-300 gold
- Side quests: 100-500 gold

---

## Implementation

```python
class WeaponUpgrade:
    def __init__(self, weapon, tier, path, cost_gold, cost_materials, stats):
        self.weapon = weapon
        self.tier = tier  # 1, 2, or 3
        self.path = path  # A, B, or None for tier 1
        self.cost_gold = cost_gold
        self.cost_materials = cost_materials  # {material_name: quantity}
        self.stats = stats  # Stat modifications

    def apply(self, weapon_instance):
        weapon_instance.damage = self.stats['damage']
        weapon_instance.attack_speed = self.stats['attack_speed']
        # Apply special effects if any
```

---

**Status:** Design complete
**Impact:** High (defines build identity and progression)
