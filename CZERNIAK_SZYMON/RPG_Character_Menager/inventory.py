#Inventory functions for the RPG Character Manager


def add_item(character, item_name, item_type="misc", bonus=0):
    #Add a new item to the character's inventory

    item_name = item_name.strip()
    item_type = item_type.strip().lower()

    if not item_name:
        print("Item name cannot be empty.")
        return None

    if not item_type:
        print("Item type cannot be empty.")
        return None

    if not isinstance(bonus, (int, float)):
        print("Bonus must be a number.")
        return None

    item = {
        "name": item_name,
        "type": item_type,
        "bonus": bonus
    }

    character["inventory"].append(item)

    return item


def remove_item(character, item_name):
    #Remove an item by name and return True or False

    for item in character["inventory"]:

        if item["name"].casefold() == item_name.strip().casefold():
            character["inventory"].remove(item)
            return True

    return False


def get_weapon_bonuses(character):
    #Return a list of bonuses from weapons only

    bonuses = []

    for item in character["inventory"]:

        if item["type"] == "weapon":
            bonuses.append(item["bonus"])

    return bonuses
