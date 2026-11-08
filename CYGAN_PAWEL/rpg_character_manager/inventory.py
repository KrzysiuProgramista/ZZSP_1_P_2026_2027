def add_item(character, item_name, item_type="misc", bonus=0):
    """Add a new item to character inventory."""
    item = {
        "name": item_name,
        "type": item_type,
        "bonus": bonus
    }
    character["inventory"].append(item)
def remove_item(character, item_name):
    """Remove an item by name. Return True or False."""
    for item in character["inventory"]:
        if item["name"].lower() == item_name.lower():
            character["inventory"].remove(item)
            return True
    return False
def get_weapon_bonuses(character):
    """Return bonuses from all weapons in inventory."""
    bonuses = []
    for item in character["inventory"]:
        if item["type"] == "weapon":
            bonuses.append(item["bonus"])
    return bonuses
