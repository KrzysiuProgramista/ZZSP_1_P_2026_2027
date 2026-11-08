#The example of the inventory

#{
#    "name": "Iron Sword",
#    "type": "weapon",
#    "bonus": 4
#}


def add_item(character,item_name,item_type='misc',bonus= 0):
    item = {
        "name": item_name, "type": item_type, "bonus":bonus
    }
    character["inventory"].append(item)

def remove_item(character,item_name):
    for item in character["inventory"]:
        if item["name"].lower() == item_name.lower():
            character["inventory"].remove(item)
            return True
        else:
            return False

def get_weapon_bonuses(character):
    bonuses = 0
    for item in character["inventory"]:
        if item["type"].lower() == "weapon":
            bonuses += item["bonus"]
        
    return bonuses