BASE_STATS = {
    "Warrior": {"hp": 120, "attack": 12, "defense": 8},
    "Mage": {"hp": 80, "attack": 15, "defense": 4},
    "Ranger": {"hp": 100, "attack": 11, "defense": 6}
}

DEFAULT_LEVEL = 1


def create_character(name, character_class="Warrior", level=1):
    """Create and return a new RPG character."""

    if not name.strip():
        raise ValueError("Character name cannot be empty.")

    if character_class not in BASE_STATS:
        raise ValueError("Unknown character class.")

    if level < 1:
        raise ValueError("Level must be at least 1.")

    return {
        "name": name,
        "class": character_class,
        "level": level,
        "inventory": []
    }


def calculate_attack(base_attack, *bonuses):
    """Calculate attack including all bonuses."""

    return base_attack + sum(bonuses)


def calculate_stats(character):
    """Calculate and return HP, attack and defense."""

    from inventory import get_weapon_bonuses

    stats = BASE_STATS[character["class"]]
    level = character["level"]

    hp = stats["hp"] + 10 * (level - 1)

    bonuses = get_weapon_bonuses(character)

    attack = calculate_attack(
        stats["attack"] + 2 * (level - 1),
        *bonuses
    )

    defense = stats["defense"] + (level - 1)

    return hp, attack, defense


def level_up(character):
    """Increase character level by one."""

    character["level"] += 1
