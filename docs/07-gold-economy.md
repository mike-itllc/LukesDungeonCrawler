# Gold Economy

## Overview
Gold is the primary currency for progression. It's used for weapon upgrades, shop purchases, and unlocking optional content. **Gold is NOT used for stat increases or levels** - only gear and utility.

## Design Goals
- **Meaningful spending:** Every purchase should feel impactful
- **Resource pressure:** Can't afford everything, must prioritize
- **No grinding required:** Normal play provides sufficient gold

---

## Gold Sources

### Combat (Primary)
- **Trash enemies:** 5-10 gold
- **Elite enemies:** 20-50 gold
- **Mini-bosses:** 100-150 gold
- **Dungeon bosses:** 200-300 gold

### Exploration (Secondary)
- **Chests:** 50-150 gold
- **Hidden rooms:** 100-200 gold
- **Secret areas:** 200-500 gold

### Side Quests (Tertiary)
- **Simple quests:** 100-200 gold
- **Complex quests:** 300-500 gold
- **Chain quests:** 500-1000 gold total

### Selling Items
- **Unwanted gear:** 50-70% of shop value
- **Materials:** 10-20 gold per common material
- **Rare materials:** Cannot sell (too valuable)

---

## Gold Sinks

### Weapon Upgrades (Primary)
- **Tier 1:** 100-200 gold
- **Tier 2:** 300-500 gold
- **Tier 3:** 500-800 gold
- **Total per weapon:** 900-1500 gold

### Shop Purchases (Secondary)
- **Consumables:** 10-30 gold each
  - Health potions: 20 gold
  - Stamina potions: 15 gold
  - Bombs: 25 gold
  - Traps: 30 gold
- **Gear:** 100-500 gold
  - Basic weapons: 100-200 gold
  - Rare weapons: 300-500 gold
  - Armor pieces: 150-400 gold

### Shop Rerolls (Tertiary)
- **First reroll:** 50 gold
- **Second reroll:** 100 gold
- **Third reroll:** 200 gold
- (Resets on new dungeon)

### Optional Unlocks (Quaternary)
- **Shortcut doors:** 200-300 gold (skip back to checkpoint)
- **Secret doors:** 300-500 gold (access treasure rooms)
- **Challenge rooms:** 100 gold entry (high reward if cleared)

---

## Gold Flow by Dungeon

### Expected Earnings
- **Dungeon 1:** ~400-500 gold
- **Dungeon 2:** ~500-600 gold
- **Dungeon 3:** ~600-700 gold
- **Dungeons 4-6:** ~700-900 gold each
- **Dungeons 7-8:** ~900-1200 gold each
- **Side quests total:** ~2000-3000 gold
- **Total available:** ~8000-10000 gold

### Expected Spending
- **Weapon upgrades:** ~2000-3000 gold (1-2 weapons fully upgraded)
- **Consumables:** ~1000-1500 gold
- **Shop gear:** ~1000-2000 gold
- **Optional unlocks:** ~500-1000 gold
- **Total needed:** ~5500-8500 gold

**Balance:** Players can afford main progression + some extras, but not everything.

---

## Shop System

### Shop Inventory
Rotates between dungeons. Each dungeon completion refreshes shop.

**Always Available:**
- Health potions (unlimited)
- Stamina potions (unlimited)
- Bombs (limited stock)

**Random Pool (4-6 items):**
- Weapons (2-3 options)
- Armor (2-3 options)
- Consumables (varies)

### Reroll Mechanic
- Player can pay gold to reroll shop inventory
- Costs increase per reroll (50 → 100 → 200)
- Resets when dungeon completed

---

## Gold Display
- **HUD:** Always visible (top right)
- **Pickup:** Shows +X gold on screen
- **Shop:** Shows current gold vs. item cost
- **Upgrade screen:** Shows cost breakdown (gold + materials)

---

## No Gold Loss on Death
Players keep gold when they die. This prevents frustration and allows risk-taking.

---

**Status:** Design complete
**Impact:** Medium (supports progression, not core mechanic)
