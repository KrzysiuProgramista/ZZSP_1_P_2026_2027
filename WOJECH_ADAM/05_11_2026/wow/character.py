from wow.inventory import get_weapon_bonuses, get_armor_bonuses, get_potion_bonuses

BASE_STATS = {
    "Warrior":  {"hp": 120, "attack": 12, "defense": 8},
    "Mage":     {"hp": 80,  "attack": 15, "defense": 4},
    "Ranger":   {"hp": 100, "attack": 11, "defense": 6},
    "Paladin":  {"hp": 140, "attack": 10, "defense": 10},
    "Assassin": {"hp": 90,  "attack": 16, "defense": 5}
}

DEFAULT_LEVEL = 1

def create_character(name, character_class="Warrior", level=1):
    return {
        "name": name,
        "class": character_class,
        "level": level,
        "inventory": []
    }

def calculate_stats(character):
    char_class = character["class"]
    level = character["level"]
    
    stats = BASE_STATS[char_class]
    
    level_hp = stats["hp"] + 10 * (level - 1)
    level_def = stats["defense"] + 1 * (level - 1)
    
    current_hp = level_hp + sum(get_potion_bonuses(character))
    current_atk = stats["attack"] + sum(get_weapon_bonuses(character))
    current_def = level_def + sum(get_armor_bonuses(character))
    
    return current_hp, current_atk, current_def

def level_up(character):
    character["level"] += 1
