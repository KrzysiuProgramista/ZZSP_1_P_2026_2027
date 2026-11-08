def add_item(character, item_name, item_type="misc", bonus=0):
#Add a new item dictionary to the character inventory
    new_item = {
        "name": item_name,
        "type": item_type,
        "bonus": bonus
    }
    character["inventory"].append(new_item)

def remove_item(character, item_name):
#Remove an item by its name. Return True if found, False otherwise
    for item in character["inventory"]:
        if item["name"].lower() == item_name.lower():
            character["inventory"].remove(item)
            return True
    return False

def _get_bonuses_by_type(character, item_type):
#Helper to extract bonus values for a specific item type
    return [item["bonus"] for item in character["inventory"] if item["type"] == item_type]

def get_weapon_bonuses(character):
#Return a list of weapon bonuses
    return _get_bonuses_by_type(character, "weapon")

def get_armor_bonuses(character):
#Return a list of armor bonuses
    return _get_bonuses_by_type(character, "armor")

def get_potion_bonuses(character):
#Return a list of potion bonuses
    return _get_bonuses_by_type(character, "potion")
