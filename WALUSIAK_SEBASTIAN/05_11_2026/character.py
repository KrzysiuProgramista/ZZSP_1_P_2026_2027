from inventory import get_weapon_bonuses

BASE_STATS = {
    "Warrior": {"hp": 120, "attack": 12, "defense": 8},
    "Mage": {"hp": 80, "attack": 15, "defense": 4},
    "Ranger": {"hp": 100, "attack": 11, "defense": 6}
}

DEFAULT_LEVEL = 1

def create_character(name, character_class="Warrior", level=DEFAULT_LEVEL):
    """Tworzy i zwraca nowy słownik z danymi postaci."""
    return {
        "name": name,
        "class": character_class,
        "level": level,
        "inventory": []
    }

def calculate_attack(base_attack, *bonuses):
    """Zwraca bazowy atak powiększony o sumę wszystkich bonusów z broni."""
    return base_attack + sum(bonuses)

def calculate_stats(character):
    """Oblicza aktualne HP, Atak oraz Obronę na podstawie poziomu i broni."""
    char_class = character["class"]
    stats = BASE_STATS[char_class]
    lvl = character["level"]

    hp = stats["hp"] + 10 * (lvl - 1)
    defense = stats["defense"] + 1 * (lvl - 1)
    weapon_bonuses = get_weapon_bonuses(character)
    base_attack = stats["attack"] + 2 * (lvl - 1)
    attack = calculate_attack(base_attack, *weapon_bonuses)

    return hp, attack, defense

def level_up(character):
    """Zwiększa poziom postaci o 1."""
    character["level"] += 1
