from character import (
    DEFAULT_CLASS,
    DEFAULT_LEVEL,
    calculate_stats,
    create_character,
    level_up,
)
from inventory import add_item, remove_item

MENU = """
==== RPG Character Manager ====
1. Create character
2. Add inventory item
3. Remove inventory item
4. Level up
5. Show character sheet
0. Exit
"""


def ask(prompt):
    return input(prompt).strip()


def ask_whole_number(prompt, minimum, default=None):
    while True:
        text = ask(prompt)
        if text == "" and default is not None:
            return default
        try:
            value = int(text)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if value < minimum:
            print(f"Please enter a number that is {minimum} or higher.")
            continue
        return value


def show_character_sheet(character):
    hp, attack, defense = calculate_stats(character)
    print(f"\n--- {character['name']} ---")
    print(f"Class: {character['class']}    Level: {character['level']}")
    print(f"HP: {hp}    Attack: {attack}    Defense: {defense}")
    print("Inventory:")
    if not character["inventory"]:
        print("  (empty)")
    for item in character["inventory"]:
        print(f"  - {item['name']} [{item['type']}, bonus {item['bonus']}]")
    print()


def create_new_character():
    name = ask("Hero name: ")
    if not name:
        print("Error: Character name cannot be empty.")
        return None
    class_text = ask(f"Class (Warrior, Mage, Ranger) [{DEFAULT_CLASS}]: ")
    character_class = class_text.title() or DEFAULT_CLASS
    level = ask_whole_number(
        f"Starting level [{DEFAULT_LEVEL}]: ", minimum=1, default=DEFAULT_LEVEL
    )
    try:
        hero = create_character(name, character_class, level)
    except ValueError as error:
        print(f"Error: {error}")
        return None
    print(f"{hero['name']} the {hero['class']} joins the Adventurers' Guild!")
    return hero


def add_inventory_item(hero):
    item_name = ask("Item name: ")
    if not item_name:
        print("The item name cannot be empty.")
        return
    item_type = ask("Item type (weapon, consumable, armor, misc) [misc]: ").lower()
    item_type = item_type or "misc"
    bonus = ask_whole_number("Bonus value [0]: ", minimum=0, default=0)
    add_item(hero, item_name, item_type, bonus)
    print(f"Added {item_name}.")


def remove_inventory_item(hero):
    item_name = ask("Item to remove: ")
    if remove_item(hero, item_name):
        print(f"Removed {item_name}.")
    else:
        print(f"No item named '{item_name}' was found. Nothing was changed.")


def level_up_hero(hero):
    new_level = level_up(hero)
    print(f"{hero['name']} reached level {new_level}!")


def main():
    hero = None
    print("Welcome to the Adventurers' Guild registry.")

    while True:
        print(MENU)
        choice = ask("Choose an option: ")

        if choice == "0":
            print("Farewell, adventurer!")
            break

        if choice == "1":
            new_hero = create_new_character()
            if new_hero is not None:
                hero = new_hero
        elif choice in {"2", "3", "4", "5"}:
            if hero is None:
                print("Create a character first (option 1).")
            elif choice == "2":
                add_inventory_item(hero)
            elif choice == "3":
                remove_inventory_item(hero)
            elif choice == "4":
                level_up_hero(hero)
            else:
                show_character_sheet(hero)
        else:
            print("Please choose a number from the menu.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
