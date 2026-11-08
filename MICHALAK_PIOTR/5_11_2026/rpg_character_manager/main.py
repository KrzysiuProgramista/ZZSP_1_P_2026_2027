"""Main program: text menu for the RPG Character Manager."""

from character import BASE_STATS, DEFAULT_LEVEL, create_character, calculate_stats, level_up
from inventory import add_item, remove_item


def show_character_sheet(character):
    """Print the character sheet with name, class, level, stats and inventory."""
    hp, attack, defense = calculate_stats(character)

    print("")
    print("========== CHARACTER SHEET ==========")
    print("Name:    ", character["name"])
    print("Class:   ", character["class"])
    print("Level:   ", character["level"])
    print("-------------------------------------")
    print("HP:      ", hp)
    print("Attack:  ", attack)
    print("Defense: ", defense)
    print("-------------------------------------")
    print("Inventory:")
    if len(character["inventory"]) == 0:
        print("  (empty)")
    else:
        for item in character["inventory"]:
            print("  -", item["name"], "| type:", item["type"], "| bonus:", item["bonus"])
    print("=====================================")


def main():
    """Run the menu in a loop until the user picks 0."""
    character = None

    while True:
        print("")
        print("--- RPG Character Manager ---")
        print("1. Create character")
        print("2. Add inventory item")
        print("3. Remove inventory item")
        print("4. Level up")
        print("5. Show character sheet")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Character name: ").strip()
            if name == "":
                print("The name can't be empty.")
            else:
                class_name = input("Class (Warrior, Mage, Ranger): ").strip().capitalize()
                if class_name not in BASE_STATS:
                    print("Unknown class. Pick Warrior, Mage or Ranger.")
                else:
                    level_text = input("Starting level (press Enter for 1): ").strip()
                    if level_text == "":
                        level = DEFAULT_LEVEL
                        character = create_character(name, class_name, level)
                        print("Character created!")
                    elif level_text.isdigit() and int(level_text) >= 1:
                        level = int(level_text)
                        character = create_character(name, class_name, level)
                        print("Character created!")
                    else:
                        print("Level must be a whole number, 1 or higher.")

        elif choice == "2":
            if character is None:
                print("Create a character first (option 1).")
            else:
                item_name = input("Item name: ").strip()
                if item_name == "":
                    print("The item name can't be empty.")
                else:
                    item_type = input("Item type (weapon, armor, misc): ").strip().lower()
                    if item_type != "weapon" and item_type != "armor" and item_type != "misc":
                        print("Unknown item type. Pick weapon, armor or misc.")
                    else:
                        bonus_text = input("Bonus (a whole number, 0 or higher): ").strip()
                        if bonus_text.isdigit():
                            add_item(character, item_name, item_type, int(bonus_text))
                            print("Item added.")
                        else:
                            print("The bonus must be a whole number, 0 or higher.")

        elif choice == "3":
            if character is None:
                print("Create a character first (option 1).")
            else:
                item_name = input("Name of the item to remove: ").strip()
                if remove_item(character, item_name):
                    print("Item removed.")
                else:
                    print("That item is not in the inventory.")

        elif choice == "4":
            if character is None:
                print("Create a character first (option 1).")
            else:
                level_up(character)
                print(character["name"], "is now level", character["level"])

        elif choice == "5":
            if character is None:
                print("Create a character first (option 1).")
            else:
                show_character_sheet(character)

        elif choice == "0":
            print("Bye!")
            break

        else:
            print("Wrong choice. Please type a number from 0 to 5.")


main()