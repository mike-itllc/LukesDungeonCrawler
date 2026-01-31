# Enemy Design

## Overview
Enemies emphasize **positioning, telegraphed attacks, and synergy**. They should punish poor inventory and positioning choices, not be stat checks.

## Design Principles
- **Telegraphed:** All attacks have clear windup
- **Readable:** Visual/audio cues before attacks
- **Fair:** Player always has time to react
- **Synergistic:** Enemies work together in groups
- **Inventory-aware:** Certain enemies require specific gear counters

---

## Enemy Archetypes

### Melee Rushers
**Examples:** Goblin, Skeleton Warrior, Corrupted Guard

**Behavior:**
- Chase player aggressively
- Simple melee attacks (1s telegraph)
- Can be kited by ranged builds

**Counter:** Keep distance, use ranged attacks or dodge

---

### Ranged Attackers
**Examples:** Goblin Archer, Fire Mage, Necromancer

**Behavior:**
- Keep distance from player
- Projectile attacks (0.5s charge)
- Retreat when player approaches

**Counter:** Close distance quickly, use shields to block projectiles

---

### Tank Enemies
**Examples:** Stone Golem, Armored Knight, Iron Construct

**Behavior:**
- Slow movement
- High HP and defense
- Heavy attacks with long telegraphs

**Counter:** Dodge attacks, use high-damage weapons, patience

---

### Swarm Enemies
**Examples:** Rats, Bats, Small Slimes

**Behavior:**
- Low HP but high numbers
- Surround player
- Individually weak, dangerous in groups

**Counter:** AOE weapons, cleaving attacks, keep moving

---

### Support Enemies
**Examples:** Healer Cultist, Buffer Shaman, Summoner

**Behavior:**
- Stay back from combat
- Heal/buff allies
- Summon additional enemies

**Counter:** PRIORITY TARGET - kill first to prevent snowball

---

### Elite Enemies
**Examples:** Mini-bosses scattered in dungeons

**Behavior:**
- Unique attack patterns
- Multiple phases
- Telegraphed special attacks
- Large gold/loot rewards

**Counter:** Learn patterns, use consumables, prepare before engaging

---

## Enemy Synergies

### Composition Examples

**"Frontline + Backline"**
- Tank enemies block player
- Ranged enemies attack from behind
- Forces player to reposition or use AOE

**"Swarm + Support"**
- Healer keeps swarm alive
- Player must prioritize healer or use AOE to overwhelm healing

**"Kiter + Punisher"**
- Ranged enemy kites player
- Melee ambushes when player chases
- Punishes tunnel vision

---

## Environmental Interactions

### Hazard Synergy
- Enemies push player toward traps
- Ranged enemies force movement into hazards
- Tank enemies block safe paths

### Terrain Use
- Flying enemies ignore obstacles
- Burrowing enemies attack from below
- Ceiling enemies drop on player

---

## Difficulty Scaling

### Early Game (Dungeons 1-2)
- Simple 1-2 enemy groups
- Obvious telegraphs
- Forgiving timing

### Mid Game (Dungeons 3-5)
- 3-4 enemy groups with synergy
- Faster telegraphs
- Environmental hazards layered in

### Late Game (Dungeons 6-8)
- 4-6 enemy groups with complex synergy
- Short telegraphs
- Multi-hazard encounters

---

## Status Effects

### Slow
- **Source:** Ice enemies, traps
- **Effect:** -50% movement speed for 3s
- **Counter:** Cleanse potion, wait it out

### Poison
- **Source:** Plant enemies, poison traps
- **Effect:** 5 damage/second for 10s
- **Counter:** Antidote, high HP pool

### Stun
- **Source:** Lightning enemies, heavy attacks
- **Effect:** Cannot move or attack for 2s
- **Counter:** High defense, avoid getting hit

### Burn
- **Source:** Fire enemies, lava
- **Effect:** 10 damage/second for 5s
- **Counter:** Fire resistance gear, roll to extinguish

---

## Enemy Stats Example

```python
class Enemy:
    def __init__(self, name, hp, damage, speed, attack_range, attack_speed, gold_drop):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.speed = speed
        self.attack_range = attack_range  # Pixels
        self.attack_speed = attack_speed  # Seconds between attacks
        self.gold_drop = gold_drop
        self.state = 'idle'  # idle, alert, attacking, hurt, dead
        self.telegraph_time = 1.0  # Warning before attack

# Example enemies
GOBLIN = Enemy("Goblin", hp=30, damage=5, speed=3.0, attack_range=32, attack_speed=2.0, gold_drop=10)
STONE_GOLEM = Enemy("Stone Golem", hp=150, damage=20, speed=1.5, attack_range=48, attack_speed=4.0, gold_drop=50)
FIRE_MAGE = Enemy("Fire Mage", hp=50, damage=15, speed=2.5, attack_range=200, attack_speed=3.0, gold_drop=30)
```

---

**Status:** Design complete
**Next:** Implement enemy AI, spawning, and combat integration
