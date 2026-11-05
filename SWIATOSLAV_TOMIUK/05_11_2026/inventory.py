WEAPON_TYPE = "weapon"


def add_item(character, item_name, item_type="misc", bonus=0):
    cleaned_name = item_name.strip()
    if not cleaned_name:
        raise ValueError("Item name cannot be empty.")
    item = {"name": cleaned_name, "type": item_type, "bonus": bonus}
    character["inventory"].append(item)
    return item


def remove_item(character, item_name):
    target = item_name.strip().lower()
    for index, item in enumerate(character["inventory"]):
        if item["name"].lower() == target:
            del character["inventory"][index]
            return True
    return False


def get_weapon_bonuses(character):
    return [
        item["bonus"]
        for item in character["inventory"]
        if item["type"] == WEAPON_TYPE
    ]
