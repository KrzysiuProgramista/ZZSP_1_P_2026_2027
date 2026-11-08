#Example of the character

#character = {
#    "name": "Aria",
#    "class": "Mage",
#    "level": 1,
#    "inventory": [
#        {"name": "Oak Staff", "type": "weapon", "bonus": 3},
#        {"name": "Health Potion", "type": "consumable", "bonus": 0}
#    ]
#}



BASE_STATS = {
    "Warrior": {"hp": 120, "attack": 12, "defense": 8},
    "Mage":    {"hp": 80,  "attack": 15, "defense": 4},
    "Ranger":  {"hp": 100, "attack": 11, "defense": 6}
}

DEFAULT_LEVEL = 1

def create_character(name,character_class="Warrior",level=1):
    """create and return a new character dict."""
    if not name.strip():
        raise ValueError("Name of Character cannot be empty,if you don't wanna be without a name")
    if character_class not in BASE_STATS:
        raise ValueError("Unknown Class")
    if level < 1:
        raise ValueError("Level Must be equal 1 or higher.")
    return {
        "name":name,
        "class":character_class,
        "level":level,
        "inventory":[]
    }

def calculate_attack(base_attack, *bonuses):
    """Return the base attack plus all bonuses"""
    return base_attack + sum(bonuses)

def calculate_stats(character):
    from inventory import get_weapon_bonuses
    stats = BASE_STATS[character["class"]]
    level = character["level"]
    hp = stats["hp"] + 10 * (level - 1)
    bonuses = get_weapon_bonuses(character)
    attack = calculate_attack(stats["attack"] + 2 * (level - 1), bonuses)
    defense = stats["defense"] + 1 * (level - 1 )
    return hp,attack,defense    

def level_up(character):
    character["level"] += 1