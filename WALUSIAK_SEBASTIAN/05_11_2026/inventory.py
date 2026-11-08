def add_item(character, item_name, item_type="misc", bonus=0):
    """Dodaje nowy przedmiot jako słownik do ekwipunku postaci."""
    new_item = {
        "name": item_name,
        "type": item_type,
        "bonus": bonus
    }
    character["inventory"].append(new_item)

def remove_item(character, item_name):
    """Usuwa przedmiot z ekwipunku po nazwie. Zwraca True jeśli usunięto, False jeśli brakuje."""
    for item in character["inventory"]:
        if item["name"].lower() == item_name.lower():
            character["inventory"].remove(item)
            return True
    return False

def get_weapon_bonuses(character):
    """Zwraca listę bonusów ze wszystkich broni znajdujących się w ekwipunku."""
    bonuses = []
    for item in character["inventory"]:
        if item["type"] == "weapon":
            bonuses.append(item["bonus"])
    return bonuses
