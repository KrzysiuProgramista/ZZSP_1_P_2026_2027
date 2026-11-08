from character import (
    DEFAULT_CLASS,
    DEFAULT_LEVEL,
    calculate_stats,
    create_character,
    level_up,
)
from inventory import add_item, remove_item

MENU_TEXT = """
==== RPG Character Manager ====
1. Create character
2. Add inventory item
3. Remove inventory item
4. Level up
5. Show character sheet
0. Exit
"""


def ask(prompt_text):
    return input(prompt_text).strip()


def ask_whole_number(prompt_text, minimum, default=None):
    while True:
        res = ask(prompt_text)
        if res == "" and default is not None:
            return default
        try:
            val = int(res)
        except ValueError:
            print("Please enter a whole number.")
            continue
        
        if val < minimum:
            print(f"Please enter a number that is {minimum} or higher.")
            continue
        return val


def show_character_sheet(character):
    hp, atk, defense = calculate_stats(character)
    print(f"\n--- {character['name']} ---")
    print(f"Class: {character['class']}    Level: {character['level']}")
    print(f"HP: {hp}    Attack: {atk}    Defense: {defense}")
    print("Inventory:")
    
    if not character["inventory"]:
        print("  (empty)")
    else:
        for itm in character["inventory"]:
            print(f"  - {itm['name']} [{itm['type']}, bonus {itm['bonus']}]")
    print()


def create_new_character():
    name = ask("Hero name: ")
    if not name:
        print("Error: Character name cannot be empty.")
        return None
        
    class_prompt = ask(f"Class (Warrior, Mage, Ranger) [{DEFAULT_CLASS}]: ")
    hero_class = class_prompt.title() or DEFAULT_CLASS
    
    lvl = ask_whole_number(f"Starting level [{DEFAULT_LEVEL}]: ", minimum=1, default=DEFAULT_LEVEL)
    
    try:
        hero = create_character(name, hero_class, lvl)
    except ValueError as err:
        print(f"Error: {err}")
        return None
        
    print(f"{hero['name']} the {hero['class']} joins the Adventurers' Guild!")
    return hero


def add_inventory_item(hero):
    name = ask("Item name: ")
    if not name:
        print("The item name cannot be empty.")
        return
        
    it_type = ask("Item type (weapon, consumable, armor, misc) [misc]: ").lower()
    it_type = it_type or "misc"
    
    bonus = ask_whole_number("Bonus value [0]: ", minimum=0, default=0)
    add_item(hero, name, it_type, bonus)
    print(f"Added {name}.")


def remove_inventory_item(hero):
    name = ask("Item to remove: ")
    if remove_item(hero, name):
        print(f"Removed {name}.")
    else:
        print(f"No item named '{name}' was found. Nothing was changed.")


def level_up_hero(hero):
    new_lvl = level_up(hero)
    print(f"{hero['name']} reached level {new_lvl}!")


def main():
    hero = None
    print("Welcome to the Adventurers' Guild registry.")

    running = True
    while running:
        print(MENU_TEXT)
        opt = ask("Choose an option: ")

        if opt == "0":
            print("Farewell, adventurer!")
            running = False
        elif opt == "1":
            new_hero = create_new_character()
            if new_hero is not None:
                hero = new_hero
        elif opt in ["2", "3", "4", "5"]:
            if hero is None:
                print("Create a character first (option 1).")
            elif opt == "2":
                add_inventory_item(hero)
            elif opt == "3":
                remove_inventory_item(hero)
            elif opt == "4":
                level_up_hero(hero)
            elif opt == "5":
                show_character_sheet(hero)
        else:
            print("Please choose a number from the menu.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
