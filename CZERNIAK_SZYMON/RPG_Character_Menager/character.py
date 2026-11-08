# Character creation and statistics for the RPG Character Manager

from inventory import get_weapon_bonuses


BASE_STATS = {
    "Warrior": {"hp": 120, "attack": 12, "defense": 8},
    "Mage": {"hp": 80, "attack": 15, "defense": 4},
    "Ranger": {"hp": 100, "attack": 11, "defense": 6}
}

DEFAULT_LEVEL = 1


def create_character(name, character_class="Warrior", level=DEFAULT_LEVEL):
    #Create and return a new RPG character dictionary

    name = name.strip()

    if not name:
        print("Character name cannot be empty.")
        return None

    if character_class not in BASE_STATS:
        print("Unknown character class.")
        return None

    if not isinstance(level, int) or level < 1:
        print("Level must be at least 1.")
        return None

    return {
        "name": name,
        "class": character_class,
        "level": level,
        "inventory": []
    }


def calculate_attack(base_attack, bonuses):
    #Calculate attack by adding all bonuses to base attack

    return base_attack + sum(bonuses)


def calculate_stats(character):
    #Calculate and return HP, attack and defense

    base = BASE_STATS[character["class"]]
    level = character["level"]

    hp = base["hp"] + 10 * (level - 1)

    weapon_bonuses = get_weapon_bonuses(character)

    attack = calculate_attack(
        base["attack"] + 2 * (level - 1),
        weapon_bonuses
    )

    defense = base["defense"] + (level - 1)

    return hp, attack, defense


def level_up(character):
    #Increase character level by one

    character["level"] += 1

    return character["level"] 
