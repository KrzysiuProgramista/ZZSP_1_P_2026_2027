"""Inventory module: adding, removing and checking items.

This file does not import character.py, so there is no circular import.
"""


def add_item(character, item_name, item_type="misc", bonus=0):
    """Add an item (as a dictionary) to the character's inventory list."""
    item = {"name": item_name, "type": item_type, "bonus": bonus}
    character["inventory"].append(item)


def remove_item(character, item_name):
    """Remove the item with this name. Return True if it was removed, False if not found."""
    for item in character["inventory"]:
        if item["name"].lower() == item_name.lower():
            character["inventory"].remove(item)
            return True
    return False


def get_weapon_bonuses(character):
    """Return a list with the bonus of every item whose type is weapon."""
    bonuses = []
    for item in character["inventory"]:
        if item["type"] == "weapon":
            bonuses.append(item["bonus"])
    return bonuses