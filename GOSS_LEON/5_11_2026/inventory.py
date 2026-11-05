def add_item(character, item_name, item_type="misc", bonus=0):

    item_name = item_name.strip()
    item_type = item_type.strip().lower()

    if not item_name:
        raise ValueError("item name cannot be empty.")

    if not item_type:
        raise ValueError("item type cannot be empty.")
    
    
    if not isinstance(bonus, (int, float)):
        raise ValueError("bonus must be a number.")

    item = {
        "type": item_type,
        "bonus": bonus,
        "name": item_name,
    }

    character["inventory"].append(item)
    return item


def remove_item(character, item_name):

    for item in character["inventory"]:

        if item["name"].casefold() == item_name.strip().casefold():
            character["inventory"].remove(item)
            return True

    return False


def get_weapon_bonuses(character):
    bonuses = []

    for item in character["inventory"]:

        if item["type"] == "weapon":
            bonuses.append(item["bonus"])

    return bonuses
