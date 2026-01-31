"""
Job (class) system implementation
All 25 jobs defined here with equipment restrictions and abilities
"""

class Job:
    """Base job class"""
    def __init__(self, name, race, role, allowed_weapons, allowed_armor, forbidden_items):
        self.name = name
        self.race = race
        self.role = role
        self.allowed_weapons = allowed_weapons
        self.allowed_armor = allowed_armor
        self.forbidden_items = forbidden_items
        self.abilities = []
    
    def can_equip(self, item):
        """Check if this job can equip the given item"""
        # Forbidden check (highest priority)
        if item.subtype in self.forbidden_items:
            return False
        
        # Check weapon restrictions
        if item.type == 'weapon' and item.subtype not in self.allowed_weapons:
            return False
        
        # Check armor restrictions
        if item.type == 'armor' and item.subtype not in self.allowed_armor:
            return False
        
        return True

# ====================
# HUMAN JOBS (5)
# ====================

class HumanFighter(Job):
    def __init__(self):
        super().__init__(
            name="Fighter",
            race="human",
            role="Balanced frontline melee",
            allowed_weapons=["one_handed_sword", "shield"],
            allowed_armor=["medium_armor"],
            forbidden_items=["two_handed_weapon", "magic_staff", "bow"]
        )

class HumanArcher(Job):
    def __init__(self):
        super().__init__(
            name="Archer",
            race="human",
            role="Ranged damage and positioning",
            allowed_weapons=["bow", "crossbow", "dagger"],
            allowed_armor=["light_armor"],
            forbidden_items=["shield", "heavy_armor", "magic_staff"]
        )

class HumanMage(Job):
    def __init__(self):
        super().__init__(
            name="Mage",
            race="human",
            role="Elemental spellcasting",
            allowed_weapons=["magic_staff", "spellbook"],
            allowed_armor=["light_robe"],
            forbidden_items=["shield", "heavy_armor", "two_handed_weapon"]
        )

class HumanPaladin(Job):
    def __init__(self):
        super().__init__(
            name="Paladin",
            race="human",
            role="Defensive melee with light magic",
            allowed_weapons=["one_handed_sword", "shield", "holy_focus"],
            allowed_armor=["light_armor", "medium_armor"],
            forbidden_items=["bow", "two_handed_weapon"]
        )

class HumanRogue(Job):
    def __init__(self):
        super().__init__(
            name="Rogue",
            race="human",
            role="Fast melee and traps",
            allowed_weapons=["dagger", "short_sword", "trap"],
            allowed_armor=["light_armor"],
            forbidden_items=["shield", "heavy_armor", "magic_staff"]
        )

# ====================
# ELF JOBS (5)
# ====================

class ElfElvenArcher(Job):
    def __init__(self):
        super().__init__(
            name="Elven Archer",
            race="elf",
            role="Long-range precision",
            allowed_weapons=["longbow", "shortbow"],
            allowed_armor=["light_armor"],
            forbidden_items=["shield", "heavy_armor", "two_handed_weapon"]
        )

class ElfSpellblade(Job):
    def __init__(self):
        super().__init__(
            name="Spellblade",
            race="elf",
            role="Hybrid melee and magic",
            allowed_weapons=["light_sword", "magic_staff", "spell_focus"],
            allowed_armor=["light_armor"],
            forbidden_items=["shield", "heavy_weapon"]
        )

class ElfDruid(Job):
    def __init__(self):
        super().__init__(
            name="Druid",
            race="elf",
            role="Nature magic and battlefield control",
            allowed_weapons=["staff", "nature_relic", "totem"],
            allowed_armor=["light_robe"],
            forbidden_items=["metal_armor", "shield", "bow"]
        )

class ElfWindDancer(Job):
    def __init__(self):
        super().__init__(
            name="Wind Dancer",
            race="elf",
            role="High mobility melee",
            allowed_weapons=["dual_daggers", "light_blade"],
            allowed_armor=["light_armor"],
            forbidden_items=["shield", "heavy_weapon", "magic_staff"]
        )

class ElfRunesage(Job):
    def __init__(self):
        super().__init__(
            name="Runesage",
            race="elf",
            role="Magical support and enhancement",
            allowed_weapons=["runic_staff", "spellbook", "relic_charm"],
            allowed_armor=["light_robe"],
            forbidden_items=["heavy_armor", "bow", "two_handed_weapon"]
        )

# ====================
# DWARF JOBS (5)
# ====================

class DwarfGuardian(Job):
    def __init__(self):
        super().__init__(
            name="Guardian",
            race="dwarf",
            role="Defensive tank",
            allowed_weapons=["shield", "one_handed_hammer"],
            allowed_armor=["heavy_armor"],
            forbidden_items=["bow", "magic_staff"]
        )

class DwarfBerserker(Job):
    def __init__(self):
        super().__init__(
            name="Berserker",
            race="dwarf",
            role="High-damage melee",
            allowed_weapons=["two_handed_axe", "two_handed_hammer"],
            allowed_armor=["medium_armor"],
            forbidden_items=["shield", "magic_staff"]
        )

class DwarfBattlesmith(Job):
    def __init__(self):
        super().__init__(
            name="Battlesmith",
            race="dwarf",
            role="Gear-focused melee fighter",
            allowed_weapons=["one_handed_weapon", "shield", "engineering_tool"],
            allowed_armor=["heavy_armor"],
            forbidden_items=["bow", "magic_staff"]
        )

class DwarfDemolitionist(Job):
    def __init__(self):
        super().__init__(
            name="Demolitionist",
            race="dwarf",
            role="Area damage and traps",
            allowed_weapons=["bomb", "explosive", "light_weapon"],
            allowed_armor=["medium_armor"],
            forbidden_items=["shield", "magic_staff"]
        )

class DwarfRuneDefender(Job):
    def __init__(self):
        super().__init__(
            name="Rune Defender",
            race="dwarf",
            role="Anti-magic tank",
            allowed_weapons=["shield", "runic_hammer"],
            allowed_armor=["heavy_armor"],
            forbidden_items=["bow", "two_handed_weapon"]
        )

# ====================
# GOLEMKIN JOBS (5)
# ====================

class GolemkinJuggernaut(Job):
    def __init__(self):
        super().__init__(
            name="Juggernaut",
            race="golemkin",
            role="Slow, unstoppable tank",
            allowed_weapons=["heavy_blunt", "massive_shield"],
            allowed_armor=["heavy_armor"],
            forbidden_items=["bow", "light_weapon", "magic_staff"]
        )

class GolemkinCrusher(Job):
    def __init__(self):
        super().__init__(
            name="Crusher",
            race="golemkin",
            role="Armor-breaking melee",
            allowed_weapons=["two_handed_hammer", "heavy_blunt"],
            allowed_armor=["heavy_armor"],
            forbidden_items=["shield", "magic_staff"]
        )

class GolemkinStonecaster(Job):
    def __init__(self):
        super().__init__(
            name="Stonecaster",
            race="golemkin",
            role="Earth-based magic",
            allowed_weapons=["earth_staff", "stone_relic"],
            allowed_armor=["light_robe"],
            forbidden_items=["bow", "shield", "light_blade"]
        )

class GolemkinWarden(Job):
    def __init__(self):
        super().__init__(
            name="Warden",
            race="golemkin",
            role="Area control and lockdown",
            allowed_weapons=["shield", "one_handed_blunt"],
            allowed_armor=["heavy_armor"],
            forbidden_items=["bow", "magic_staff"]
        )

class GolemkinObelisk(Job):
    def __init__(self):
        super().__init__(
            name="Obelisk",
            race="golemkin",
            role="Stationary power",
            allowed_weapons=["heavy_weapon", "defensive_relic"],
            allowed_armor=["heavy_armor"],
            forbidden_items=["light_weapon", "bow"]
        )

# ====================
# UMBRAL JOBS (5)
# ====================

class UmbralShadeblade(Job):
    def __init__(self):
        super().__init__(
            name="Shadeblade",
            race="umbral",
            role="Stealth assassin",
            allowed_weapons=["dagger", "short_blade", "shadow_relic"],
            allowed_armor=["light_armor"],
            forbidden_items=["shield", "heavy_armor", "bow"]
        )

class UmbralHexer(Job):
    def __init__(self):
        super().__init__(
            name="Hexer",
            race="umbral",
            role="Curse-based magic",
            allowed_weapons=["curse_staff", "dark_spellbook"],
            allowed_armor=["light_robe"],
            forbidden_items=["shield", "heavy_armor", "two_handed_weapon"]
        )

class UmbralNightArcher(Job):
    def __init__(self):
        super().__init__(
            name="Night Archer",
            race="umbral",
            role="Long-range debuff damage",
            allowed_weapons=["shadow_bow"],
            allowed_armor=["light_armor"],
            forbidden_items=["shield", "heavy_weapon"]
        )

class UmbralPhantom(Job):
    def __init__(self):
        super().__init__(
            name="Phantom",
            race="umbral",
            role="Evasion-focused survival",
            allowed_weapons=["light_blade", "relic"],
            allowed_armor=["light_armor"],
            forbidden_items=["shield", "heavy_armor"]
        )

class UmbralVoidAdept(Job):
    def __init__(self):
        super().__init__(
            name="Void Adept",
            race="umbral",
            role="High-risk shadow magic",
            allowed_weapons=["void_staff", "cursed_relic"],
            allowed_armor=["light_robe"],
            forbidden_items=["shield", "heavy_armor"]
        )

# ====================
# JOB REGISTRY
# ====================

ALL_JOBS = {
    'human': [HumanFighter(), HumanArcher(), HumanMage(), HumanPaladin(), HumanRogue()],
    'elf': [ElfElvenArcher(), ElfSpellblade(), ElfDruid(), ElfWindDancer(), ElfRunesage()],
    'dwarf': [DwarfGuardian(), DwarfBerserker(), DwarfBattlesmith(), DwarfDemolitionist(), DwarfRuneDefender()],
    'golemkin': [GolemkinJuggernaut(), GolemkinCrusher(), GolemkinStonecaster(), GolemkinWarden(), GolemkinObelisk()],
    'umbral': [UmbralShadeblade(), UmbralHexer(), UmbralNightArcher(), UmbralPhantom(), UmbralVoidAdept()]
}

def get_jobs_for_race(race):
    """Get all available jobs for a given race"""
    return ALL_JOBS.get(race, [])

def get_job(race, job_name):
    """Get specific job by race and name"""
    jobs = get_jobs_for_race(race)
    for job in jobs:
        if job.name.lower() == job_name.lower():
            return job
    return None
