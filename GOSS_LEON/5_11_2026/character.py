from inventory import get_weapon_bonuses


BASE_STATS = {
    "warrior": {"hp": 120, "attack": 12, "defense": 8},
    "mage": {"hp": 80, "attack": 15, "defense": 4},
    "ranger": {"hp": 100, "attack": 11, "defense": 6}
}

DEFAULT_LEVEL = 1


def create_character(name, character_class="warrior", level=DEFAULT_LEVEL):

    name = name.strip()

    if not name:
        raise ValueError("Character name cannot be empty.")

    if character_class not in BASE_STATS:
        raise ValueError("Unknown character class.")

    if not isinstance(level, int) or level < 1:
        raise ValueError("Level must be at least 1.")

    return {
        "level": level,
        "inventory": [],
        "name": name,
        "class": character_class,

    }


def calculate_attack(base_attack, bonuses):

    return base_attack + sum(bonuses)


def calculate_stats(character):

    base = BASE_STATS[character["class"]]
    level = character["level"]

    hp = base["HP"] + 10 (level - 1)

    weapon_bonuses = get_weapon_bonuses(character)

    attack = calculate_attack(
        base["attack"] + 2 * (level - 1),
        *weapon_bonuses
    )

    defense = base["defense"] + (level - 1)

    return hp, attack, defense


def level_up(character):

    character["level"] += 1

    return character["level"] 
