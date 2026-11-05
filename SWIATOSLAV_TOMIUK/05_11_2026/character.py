from inventory import get_weapon_bonuses

BASE_STATS = {
    "Warrior": {"hp": 120, "attack": 12, "defense": 8},
    "Mage": {"hp": 80, "attack": 15, "defense": 4},
    "Ranger": {"hp": 100, "attack": 11, "defense": 6},
}
DEFAULT_CLASS = "Warrior"
DEFAULT_LEVEL = 1


def create_character(name, character_class=DEFAULT_CLASS, level=DEFAULT_LEVEL):
    if not name or not name.strip():
        raise ValueError("Character name cannot be empty.")
    if character_class not in BASE_STATS:
        raise ValueError(
            f"Unknown class '{character_class}'. Choose Warrior, Mage or Ranger."
        )
    if level < 1:
        raise ValueError("Level must be at least 1.")
    return {
        "name": name.strip(),
        "class": character_class,
        "level": level,
        "inventory": [],
    }


def calculate_attack(base_attack, *bonuses):
    return base_attack + sum(bonuses)


def calculate_stats(character):
    base = BASE_STATS[character["class"]]
    extra_levels = character["level"] - DEFAULT_LEVEL

    hp = base["hp"] + 10 * extra_levels
    base_attack = base["attack"] + 2 * extra_levels
    attack = calculate_attack(base_attack, *get_weapon_bonuses(character))
    defense = base["defense"] + 1 * extra_levels
    return hp, attack, defense


def level_up(character):
    character["level"] += 1
    return character["level"]
