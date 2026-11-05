
def add_item(character, name, category="misc", item_bonus=0):

    name = name.strip()
    category = category.lower().strip()

    if len(name) == 0:
        raise ValueError("item name cannot be empty.")

    if len(category) == 0:
        raise ValueError("item type cannot be empty.")

    if isinstance(item_bonus, (int, float)) == False:
        raise ValueError("bonus must be a number.")

    new_item = {
        "name": name,
        "type": category,
        "bonus": item_bonus
    }

    character["inventory"].append(new_item)

    return new_item


def remove_item(character, name):

    inventory = character["inventory"]
    searched_name = name.strip().casefold()

    for i, item in enumerate(inventory):
        current_name = item["name"].casefold()

        if current_name == searched_name:
            inventory.pop(i)
            return True

    return False


def get_weapon_bonuses(character):

    weapon_bonuses = [
        item["bonus"]
        for item in character["inventory"]
        if item["type"] == "weapon"
    ]

    return weapon_bonuses
