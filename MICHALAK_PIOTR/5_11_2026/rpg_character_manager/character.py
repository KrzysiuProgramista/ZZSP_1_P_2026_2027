"""Character module: creating characters, calculating stats and leveling up."""

from inventory import get_weapon_bonuses

DEFAULT_LEVEL = 1

BASE_STATS = {
    "Warrior": {"hp": 120, "attack": 15, "defense": 10},
    "Mage": {"hp": 80, "attack": 20, "defense": 4},
    "Ranger": {"hp": 100, "attack": 17, "defense": 7},
}


def create_character(name, character_class="Warrior", level=1):
    """Create a new character dictionary and return it."""
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "inventory": [],
    }
    return character


def calculate_attack(base_attack, *bonuses):
    """Add the base attack and any number of bonuses together and return the result."""
    return base_attack + sum(bonuses)


def calculate_stats(character):
    """Work out the current HP, attack and defense and return them as a tuple."""
    base = BASE_STATS[character["class"]]
    level = character["level"]

    hp = base["hp"] + 10 * (level - 1)
    defense = base["defense"] + 1 * (level - 1)

    weapon_bonuses = get_weapon_bonuses(character)
    attack = calculate_attack(base["attack"], *weapon_bonuses)

    return hp, attack, defense


def level_up(character):
    """Increase the level of the character by 1."""
    character["level"] = character["level"] + 1
