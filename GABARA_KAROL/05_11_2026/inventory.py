WEAPON_TYPE = "weapon"


def add_item(character, item_name, item_type="misc", bonus=0):
    name_trimmed = item_name.strip()
    if not name_trimmed:
        raise ValueError("Item name cannot be empty.")
    
    new_item = {"name": name_trimmed, "type": item_type, "bonus": bonus}
    character["inventory"].append(new_item)
    return new_item


def remove_item(character, item_name):
    target_name = item_name.strip().lower()
    inv = character["inventory"]
    
    for idx in range(len(inv)):
        if inv[idx]["name"].lower() == target_name:
            inv.pop(idx)
            return True
    return False


def get_weapon_bonuses(character):
    bonuses_list = []
    for item in character["inventory"]:
        if item["type"] == WEAPON_TYPE:
            bonuses_list.append(item["bonus"])
    return bonuses_list
