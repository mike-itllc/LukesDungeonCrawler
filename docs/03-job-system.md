# Job (Class) System

## Overview
Each of the 5 races has 4-5 jobs, totaling 25 unique builds. Jobs determine weapon/armor access, abilities, and combat role. **Jobs must not override race traits** - they add on top of them.

## Design Principles
- **Weapon restrictions:** Jobs define what can be equipped
- **Role clarity:** Each job has a distinct playstyle
- **No trait override:** Race traits always apply
- **Forbidden = blocked:** If a tool is forbidden, it CANNOT be equipped

---

## 🧍 HUMAN JOBS (5)

### Fighter
**Role:** Balanced frontline melee

**Allowed Equipment:**
- One-handed swords ✓
- Shields ✓
- Medium armor ✓

**Forbidden:**
- Heavy two-handed weapons ✗
- Magic staves ✗
- Bows ✗

**Abilities:**
- **Shield Bash:** Stun enemy with shield (if equipped)
- **Parry:** Perfect block window for counterattack
- **Steady Stance:** Reduced knockback

---

### Archer
**Role:** Ranged damage and positioning

**Allowed Equipment:**
- Bows ✓
- Crossbows ✓
- Light armor ✓
- Daggers (secondary) ✓

**Forbidden:**
- Shields ✗
- Heavy armor ✗
- Magic staves ✗

**Abilities:**
- **Aimed Shot:** Charged arrow for bonus damage
- **Quick Step:** Short dash backward
- **Piercing Arrow:** Arrow penetrates multiple enemies

---

### Mage
**Role:** Elemental spellcasting

**Allowed Equipment:**
- Magic staves ✓
- Spellbooks ✓
- Light robes ✓

**Forbidden:**
- Shields ✗
- Heavy armor ✗
- Two-handed melee weapons ✗

**Abilities:**
- **Fireball:** Ranged AOE damage
- **Ice Shard:** Slow enemy movement
- **Arcane Barrier:** Temporary damage shield

---

### Paladin
**Role:** Defensive melee with light magic

**Allowed Equipment:**
- One-handed swords ✓
- Shields ✓
- Light to medium armor ✓
- Holy spell focus ✓

**Forbidden:**
- Bows ✗
- Heavy two-handed weapons ✗

**Abilities:**
- **Holy Strike:** Melee attack with light damage bonus
- **Blessing:** Heal self or ally
- **Divine Shield:** Temporary invulnerability (long cooldown)

---

### Rogue
**Role:** Fast melee and traps

**Allowed Equipment:**
- Daggers ✓
- Short swords ✓
- Traps ✓
- Light armor ✓

**Forbidden:**
- Shields ✗
- Heavy armor ✗
- Magic staves ✗

**Abilities:**
- **Backstab:** Bonus damage from behind
- **Smoke Bomb:** Drop trap, become invisible briefly
- **Poison Blade:** Apply DoT to attacks

---

## 🧝 ELF JOBS (5)

### Elven Archer
**Role:** Long-range precision

**Allowed Equipment:**
- Longbows ✓
- Shortbows ✓
- Light armor ✓

**Forbidden:**
- Shields ✗
- Heavy armor ✗
- Two-handed melee weapons ✗

**Abilities:**
- **Multi-Shot:** Fire 3 arrows at once
- **Eagle Eye:** Increased range and accuracy
- **Evasive Roll:** Extra i-frames (synergizes with elf speed)

---

### Spellblade
**Role:** Hybrid melee and magic

**Allowed Equipment:**
- Light swords ✓
- Magic staves ✓
- Spell focus items ✓
- Light armor ✓

**Forbidden:**
- Shields ✗
- Heavy weapons ✗

**Abilities:**
- **Elemental Blade:** Enchant weapon with fire/ice/lightning
- **Blink Strike:** Teleport to enemy and slash
- **Spell Parry:** Reflect magic attacks

---

### Druid
**Role:** Nature magic and battlefield control

**Allowed Equipment:**
- Staves ✓
- Nature relics ✓
- Totems ✓
- Light robes ✓

**Forbidden:**
- Metal armor ✗
- Shields ✗
- Bows ✗

**Abilities:**
- **Entangling Roots:** Trap enemies in place
- **Wild Shape:** Transform into animal (bear, wolf, hawk)
- **Rejuvenation:** Heal over time aura

---

### Wind Dancer
**Role:** High mobility melee

**Allowed Equipment:**
- Dual daggers ✓
- Light blades ✓
- Light armor ✓

**Forbidden:**
- Shields ✗
- Heavy weapons ✗
- Magic staves ✗

**Abilities:**
- **Whirlwind Strike:** Spin attack hitting all around
- **Air Dash:** Dash through enemies (invulnerable)
- **Momentum:** Movement speed increases with consecutive hits

---

### Runesage
**Role:** Magical support and enhancement

**Allowed Equipment:**
- Runic staves ✓
- Spellbooks ✓
- Relic charms ✓

**Forbidden:**
- Heavy armor ✗
- Bows ✗
- Two-handed melee weapons ✗

**Abilities:**
- **Rune Trap:** Place magical trap on ground
- **Haste Rune:** Increase ally speed
- **Ward:** Reduce incoming damage temporarily

---

## 🧔 DWARF JOBS (5)

### Guardian
**Role:** Defensive tank

**Allowed Equipment:**
- Shields ✓
- One-handed hammers ✓
- Heavy armor ✓

**Forbidden:**
- Bows ✗
- Magic staves ✗

**Abilities:**
- **Shield Wall:** Block all frontal damage
- **Taunt:** Force enemies to attack you
- **Iron Skin:** Reduce damage taken (stacks with dwarf trait)

---

### Berserker
**Role:** High-damage melee

**Allowed Equipment:**
- Two-handed axes ✓
- Two-handed hammers ✓
- Medium armor ✓

**Forbidden:**
- Shields ✗
- Magic staves ✗

**Abilities:**
- **Rage:** Increase damage, lose defense
- **Cleave:** Swing hits multiple enemies
- **Bloodlust:** Heal on kill

---

### Battlesmith
**Role:** Gear-focused melee fighter

**Allowed Equipment:**
- One-handed weapons ✓
- Shields ✓
- Heavy armor ✓
- Engineering tools ✓

**Forbidden:**
- Bows ✗
- Pure magic staves ✗

**Abilities:**
- **Repair:** Restore armor durability mid-combat
- **Fortify:** Increase defense temporarily
- **Gear Toss:** Throw wrench/tool for ranged damage

---

### Demolitionist
**Role:** Area damage and traps

**Allowed Equipment:**
- Bombs ✓
- Explosives ✓
- Light weapons ✓
- Medium armor ✓

**Forbidden:**
- Shields ✗
- Magic staves ✗

**Abilities:**
- **Sticky Bomb:** Attach bomb to enemy
- **Blast Zone:** Drop AOE explosion trap
- **Powder Keg:** Massive explosion (high cooldown)

---

### Rune Defender
**Role:** Anti-magic tank

**Allowed Equipment:**
- Shields ✓
- Runic hammers ✓
- Heavy armor ✓

**Forbidden:**
- Bows ✗
- Two-handed weapons ✗

**Abilities:**
- **Rune Shield:** Reflect magic attacks
- **Dispel:** Remove buffs from enemies
- **Magic Resistance:** Reduce magic damage taken

---

## 🪨 GOLEMKIN JOBS (5)

### Juggernaut
**Role:** Slow, unstoppable tank

**Allowed Equipment:**
- Heavy blunt weapons ✓
- Massive shields ✓

**Forbidden:**
- Bows ✗
- Light weapons ✗
- Magic staves ✗

**Abilities:**
- **Unstoppable Force:** Charge forward, knockback all
- **Stone Barrier:** Create wall
- **Ground Slam:** AOE knockdown

---

### Crusher
**Role:** Armor-breaking melee

**Allowed Equipment:**
- Two-handed hammers ✓
- Heavy blunt weapons ✓

**Forbidden:**
- Shields ✗
- Magic staves ✗

**Abilities:**
- **Shatter:** Destroy enemy armor
- **Earthquake:** Ground stomp stuns enemies
- **Momentum Swing:** Charge attack for massive damage

---

### Stonecaster
**Role:** Earth-based magic

**Allowed Equipment:**
- Earth staves ✓
- Stone relics ✓

**Forbidden:**
- Bows ✗
- Shields ✗
- Light blades ✗

**Abilities:**
- **Stone Spike:** Summon spike from ground
- **Rock Armor:** Temporary defense boost
- **Boulder Toss:** Throw giant rock

---

### Warden
**Role:** Area control and lockdown

**Allowed Equipment:**
- Shields ✓
- One-handed blunt weapons ✓

**Forbidden:**
- Bows ✗
- Magic staves ✗

**Abilities:**
- **Stone Prison:** Trap enemy in rock
- **Earthen Grasp:** Roots enemy in place
- **Guardian Stance:** Reduce all damage taken (immobile)

---

### Obelisk
**Role:** Stationary power

**Allowed Equipment:**
- Heavy weapons ✓
- Defensive relics ✓

**Forbidden:**
- Light weapons ✗
- Bows ✗

**Abilities:**
- **Anchor:** Root self, gain massive defense
- **Gravity Well:** Pull enemies toward you
- **Immutable:** Cannot be moved or knocked back

---

## 🌑 UMBRAL JOBS (5)

### Shadeblade
**Role:** Stealth assassin

**Allowed Equipment:**
- Daggers ✓
- Short blades ✓
- Shadow relics ✓

**Forbidden:**
- Shields ✗
- Heavy armor ✗
- Bows ✗

**Abilities:**
- **Shadow Strike:** Teleport behind enemy and stab
- **Vanish:** Become invisible for short time
- **Execution:** Instant kill low-hp enemies

---

### Hexer
**Role:** Curse-based magic

**Allowed Equipment:**
- Curse staves ✓
- Dark spellbooks ✓

**Forbidden:**
- Shields ✗
- Heavy armor ✗
- Two-handed weapons ✗

**Abilities:**
- **Hex:** Apply debuff (slow, weaken, blind)
- **Life Drain:** Steal HP from enemy
- **Curse Mark:** Mark enemy, others deal bonus damage

---

### Night Archer
**Role:** Long-range debuff damage

**Allowed Equipment:**
- Shadow bows ✓
- Light armor ✓

**Forbidden:**
- Shields ✗
- Heavy weapons ✗

**Abilities:**
- **Shadow Arrow:** Arrow applies darkness (reduce vision)
- **Marked Shot:** Tag enemy, next hit deals bonus damage
- **Ghost Shot:** Arrow passes through walls

---

### Phantom
**Role:** Evasion-focused survival

**Allowed Equipment:**
- Light blades ✓
- Relics ✓

**Forbidden:**
- Shields ✗
- Heavy armor ✗

**Abilities:**
- **Phase:** Become intangible briefly
- **Afterimage:** Leave decoy behind when dodging
- **Spectral Form:** Move through enemies

---

### Void Adept
**Role:** High-risk shadow magic

**Allowed Equipment:**
- Void staves ✓
- Cursed relics ✓

**Forbidden:**
- Shields ✗
- Heavy armor ✗

**Abilities:**
- **Void Bolt:** High damage, drain HP on cast
- **Dark Pact:** Sacrifice HP for massive damage boost
- **Entropy:** Drain life from area around you

---

## Implementation Structure

```python
class Job:
    def __init__(self, name, role, allowed_weapons, allowed_armor, forbidden_items):
        self.name = name
        self.role = role
        self.allowed_weapons = allowed_weapons
        self.allowed_armor = allowed_armor
        self.forbidden_items = forbidden_items
        self.abilities = []  # List of Ability objects
    
    def can_equip(self, item):
        # Check if job allows this item type
        if item.type in self.forbidden_items:
            return False
        if item.type == 'weapon' and item.subtype not in self.allowed_weapons:
            return False
        if item.type == 'armor' and item.subtype not in self.allowed_armor:
            return False
        return True

class Ability:
    def __init__(self, name, description, cooldown, effect):
        self.name = name
        self.description = description
        self.cooldown = cooldown  # Seconds
        self.current_cooldown = 0
        self.effect = effect  # Function reference
```

## Equipment Validation Flow
1. Player picks up item
2. Check: Is item type forbidden by job? → Reject
3. Check: Is item type in allowed list? → Accept
4. Race traits still apply (e.g., Elf can't wear heavy armor even if job allows)

## Key Rule
**"Forbidden beats allowed"**
If an item is explicitly forbidden, the job CANNOT use it, period.

---

**Status:** Design complete, ready for implementation
**Complexity:** HIGH (25 jobs × 3-4 abilities each = ~75-100 abilities to code)
