# Combat System - Player Controller & Combat Feel

## Overview
Top-down action combat inspired by classic Zelda games. Combat must feel **readable, responsive, and fair**. Enemy attacks are telegraphed, positioning matters, and inventory choices affect combat effectiveness.

## Design Goals
- **Readable:** Clear visual feedback for attacks, dodges, hit states
- **Responsive:** Tight controls, instant feedback
- **Fair:** Telegraphed enemy attacks, no cheap shots
- **Inventory-driven:** Your loadout dramatically affects combat options

---

## Player Actions

### Movement
- **Input:** WASD or Arrow keys
- **Speed:** Based on race (Elf fastest, Golemkin slowest)
- **Diagonal:** Normalized speed (no faster diagonals)
- **Collision:** Blocked by walls, pushes against enemies

### Attack (Melee)
- **Input:** Left mouse click or J key
- **Behavior:**
  - Short windup animation (~0.1-0.2s)
  - Hitbox appears in attack direction
  - Brief recovery (~0.2-0.3s)
  - Cannot move during attack
- **Damage:** Based on equipped weapon
- **Direction:** 8-way directional attacks (up, down, left, right, diagonals)

### Attack (Ranged)
- **Input:** Left mouse click (if bow/staff equipped)
- **Behavior:**
  - Charge time (hold click to charge)
  - Release to fire projectile
  - Projectile travels in aimed direction
  - Can move while charging (but slower)
- **Ammo:** Some ranged weapons use consumable ammo

### Dodge Roll
- **Input:** Spacebar
- **Behavior:**
  - Roll in current movement direction
  - ~0.5s duration
  - Invulnerability frames (i-frames) during roll
  - Short cooldown after (~1s)
  - Costs stamina
- **Race modifiers:**
  - Elf: Extra i-frames (+50%)
  - Umbral: Extended i-frames (+50%)
  - Golemkin: **Cannot dodge** (too heavy)

### Block (Shield Required)
- **Input:** Hold Right mouse or K key
- **Behavior:**
  - Raise shield, face mouse direction
  - Blocks damage from frontal arc
  - Stamina drains while blocking
  - Heavy hits can stagger (deplete stamina)
- **Cannot:** Attack while blocking

### Use Item (Consumable)
- **Input:** Number keys 1-4 (quick slots)
- **Behavior:**
  - Instant use (potions, bombs, traps)
  - Brief animation (can be interrupted by dodge)
- **Cooldown:** Global item cooldown (~0.5s)

---

## Combat Stats

### Player Stats
- **HP:** Health points (race-dependent)
- **Stamina:** Used for dodge, block, special attacks
- **Damage:** Based on equipped weapon + racial bonuses
- **Defense:** Based on equipped armor
- **Speed:** Movement speed (race-dependent)

### Weapon Stats
- **Damage:** Base damage dealt
- **Attack Speed:** Time between attacks
- **Range:** Melee range or projectile distance
- **Stamina Cost:** Some weapons drain stamina

### Armor Stats
- **Defense:** Flat damage reduction
- **Weight:** Affects movement speed (light/medium/heavy)

---

## Damage Calculation

### Basic Formula
```
Damage Dealt = (Weapon Damage + Racial Bonus) - (Armor Defense)
Minimum Damage = 1 (always deal at least 1 damage)
```

### Critical Hits
- **Chance:** Base 10% (Dwarf +10% = 20%)
- **Multiplier:** 1.5x damage
- **Visual:** Different hit effect, larger numbers

### Elemental Damage (if applicable)
- Fire: Burn DoT
- Ice: Slow movement
- Lightning: Stun chance
- Dark: HP drain

---

## Hit Detection

### Player Attacking Enemy
1. Attack animation plays
2. Hitbox spawns in attack direction
3. Check overlap with enemy hitbox
4. If hit:
   - Deal damage
   - Apply knockback
   - Play hit sound + visual
   - Short hitstun on enemy

### Enemy Attacking Player
1. Enemy telegraph animation (~0.5-1s warning)
2. Attack animation plays
3. Hitbox spawns
4. Check overlap with player
5. If hit AND player not in i-frames:
   - Deal damage to player
   - Knockback player
   - Play hurt sound + visual
   - Brief invulnerability (~0.3s)

---

## Enemy Telegraphing

**All enemy attacks MUST be telegraphed** to keep combat fair.

### Telegraph Types
1. **Wind-up animation:** Enemy pulls back, changes color
2. **Visual indicator:** Red circle/cone shows attack area
3. **Audio cue:** Sound effect before attack
4. **Timing:** At least 0.5s warning for basic attacks, 1s+ for big attacks

### Examples
- **Goblin Slash:** Raises weapon, red arc appears, then swings
- **Ogre Slam:** Lifts club overhead, ground cracks appear, then smash
- **Mage Fireball:** Staff glows, magic circle appears, then fires

---

## Combat States

### Player States
- **Idle:** Standing still, can take any action
- **Moving:** Walking, can attack/dodge
- **Attacking:** Animation locked, cannot move
- **Dodging:** Rolling, invulnerable
- **Blocking:** Shielding, cannot attack
- **Hurt:** Hit by enemy, brief stagger
- **Dead:** HP = 0, respawn at checkpoint

### Enemy States
- **Idle:** Wandering or patrolling
- **Alert:** Spotted player, moving to engage
- **Attacking:** Telegraphing or executing attack
- **Hurt:** Taking damage, brief stagger
- **Dead:** HP = 0, drop loot

---

## Stamina System

### Stamina Usage
- **Dodge:** 20 stamina
- **Block (per second):** 10 stamina/s
- **Special attacks:** Varies by ability

### Stamina Regen
- **Passive:** 15 stamina/second (when not blocking)
- **Out of stamina:** Cannot dodge, blocking automatically drops

### Race Differences
- Human: 100 stamina (balanced)
- Elf: 120 stamina (high mobility)
- Dwarf: 80 stamina (low mobility)
- Golemkin: 60 stamina (no dodge anyway)
- Umbral: 110 stamina (evasion-focused)

---

## Combat Feel Checklist
- ✅ Attacks have clear windup and recovery
- ✅ Hit feedback is immediate and satisfying
- ✅ Enemy attacks are telegraphed fairly
- ✅ Dodge roll has i-frames and feels responsive
- ✅ Blocking requires positioning and stamina management
- ✅ Camera stays centered on player
- ✅ No cheap deaths (player always had a chance to react)

---

## Implementation Notes

```python
class CombatController:
    def __init__(self, player):
        self.player = player
        self.attack_cooldown = 0
        self.dodge_cooldown = 0
        self.blocking = False
    
    def update(self, dt):
        # Update cooldowns
        self.attack_cooldown = max(0, self.attack_cooldown - dt)
        self.dodge_cooldown = max(0, self.dodge_cooldown - dt)
        
        # Regenerate stamina
        if not self.blocking:
            self.player.stamina = min(
                self.player.max_stamina,
                self.player.stamina + 15 * dt
            )
    
    def attack(self):
        if self.attack_cooldown > 0:
            return False
        if self.player.state == 'attacking':
            return False
        
        # Start attack
        self.player.state = 'attacking'
        self.attack_cooldown = self.player.weapon.attack_speed
        return True
    
    def dodge(self):
        if self.dodge_cooldown > 0:
            return False
        if self.player.stamina < 20:
            return False
        if self.player.race == 'golemkin':
            return False  # Golemkin cannot dodge
        
        # Start dodge
        self.player.state = 'dodging'
        self.player.stamina -= 20
        self.dodge_cooldown = 1.0
        return True
    
    def start_block(self):
        if not self.player.has_shield:
            return False
        self.blocking = True
    
    def stop_block(self):
        self.blocking = False
```

---

**Status:** Design complete, ready for implementation
**Priority:** HIGH (core gameplay loop depends on this)
