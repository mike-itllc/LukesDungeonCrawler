# Luke's Dungeon Crawler

A 2D top-down action RPG dungeon crawler inspired by classic Zelda games with deep inventory management and build variety.

## Core Pillars
- **Limited slot-based inventory** - Every item competes for space
- **Race + Job system** - 5 races × 5 jobs = 25 unique builds
- **Real-time top-down combat** - Dodge, block, attack, position
- **8 themed dungeons** - ~1 hour each, unique mechanics
- **Branching weapon upgrades** - Lock into playstyles
- **Gold economy** - Upgrades, shops, optional paths
- **Environmental storytelling** - No long cutscenes
- **Multiple endings** - Based on race, job, inventory, choices

## Tech Stack
- **Engine:** Python + Pygame
- **Art:** Pixel art (16x16 or 32x32 tiles)
- **Design:** Modular, data-driven systems

## Project Structure
```
LukesDungeonCrawler/
├── src/              # Source code
│   ├── core/         # Core game systems
│   ├── entities/     # Player, enemies, NPCs
│   ├── items/        # Inventory, equipment, consumables
│   ├── dungeon/      # Dungeon generation, rooms
│   ├── combat/       # Combat mechanics
│   └── ui/           # Menus, HUD, inventory UI
├── assets/           # Art, sound, data
│   ├── sprites/
│   ├── sounds/
│   └── data/         # JSON/YAML configs
├── docs/             # Design documents
└── tests/            # Unit tests
```

## Development Roadmap

### Phase 1: Core Systems
1. ✅ Project setup
2. ⏳ Inventory system (CRITICAL)
3. ⏳ Race system
4. ⏳ Job system
5. ⏳ Player controller & combat

### Phase 2: Content
6. ⏳ Dungeon structure
7. ⏳ Dungeon themes
8. ⏳ Enemy design
9. ⏳ Dungeon bosses
10. ⏳ Final boss

### Phase 3: Systems & Polish
11. ⏳ Weapon upgrade system
12. ⏳ Gold economy
13. ⏳ Side quest system
14. ⏳ Difficulty scaling
15. ⏳ Narrative integration
16. ⏳ Balance pass
17. ⏳ Endings

## Running the Game
```bash
python src/main.py
```

## Design Constraints
- **NO** level-based stat increases (skills come from gear/jobs)
- **NO** pure stat inflation difficulty scaling
- **NO** long cutscenes
- **KEEP** inventory pressure as core tension
- **KEEP** job/race identity clear and distinct

## Story (Brief)
The Deep Vault - an ancient dungeon said to hold unimaginable power. You are one of many who dares to delve its depths. Your race, your training (job), and your choices will determine your fate.

---

Built for Luke by Cooper (AI) 🛠️
