from inventory import get_weapon_bonuses

STATS_TABLE = {
    "Warrior": {"hp": 120, "attack": 12, "defense": 8},
    "Mage": {"hp": 80, "attack": 15, "defense": 4},
    "Ranger": {"hp": 100, "attack": 11, "defense": 6},
}
DEFAULT_CLASS = "Warrior"
DEFAULT_LEVEL = 1


def create_character(name, character_class=DEFAULT_CLASS, level=DEFAULT_LEVEL):
    clean_name = name.strip() if name else ""
    if not clean_name:
        raise ValueError("Character name cannot be empty.")
    if character_class not in STATS_TABLE:
        raise ValueError(f"Unknown class '{character_class}'. Choose Warrior, Mage or Ranger.")
    if level < 1:
        raise ValueError("Level must be at least 1.")
    
    return {
        "name": clean_name,
        "class": character_class,
        "level": level,
        "inventory": []
    }


def calculate_attack(base_attack, *bonuses):
    total_bonus = 0
    for num in bonuses:
        total_bonus += num
    return base_attack + total_bonus


def calculate_stats(character):
    cls = character["class"]
    lvl_diff = character["level"] - DEFAULT_LEVEL
    
    base_hp = STATS_TABLE[cls]["hp"]
    base_atk = STATS_TABLE[cls]["attack"]
    base_def = STATS_TABLE[cls]["defense"]

    hp = base_hp + (10 * lvl_diff)
    raw_attack = base_atk + (2 * lvl_diff)
    attack = calculate_attack(raw_attack, *get_weapon_bonuses(character))
    defense = base_def + (1 * lvl_diff)
    
    return hp, attack, defense


def level_up(character):
    character["level"] += 1
    return character["level"]
