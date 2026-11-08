# Main menu and user interface for the RPG Character Manager

from character import create_character, calculate_stats, level_up
from inventory import add_item, remove_item


def show_character_sheet(character):
    # Display character information, stats and inventory
    hp, attack, defense = calculate_stats(character)

    print("\n" + "=" * 36)
    print("       CHARACTER SHEET")
    print("=" * 36)

    print(f"Name:    {character['name']}")
    print(f"Class:   {character['class']}")
    print(f"Level:   {character['level']}")

    print("-" * 36)
    print(f"HP:      {hp}")
    print(f"Attack:  {attack}")
    print(f"Defense: {defense}")

    print("-" * 36)
    print("Inventory:")

    if character["inventory"]:
        for number, item in enumerate(character["inventory"], start=1):
            print(
                f"{number}. {item['name']} "
                f"({item['type']}, bonus: {item['bonus']})"
            )
    else:
        print("Your inventory is empty.")

    print("=" * 36)


def ask_for_integer(prompt, minimum=0):
    # Ask the user for a valid integer
    while True:
        value = input(prompt).strip()

        if value.isdigit():
            value = int(value)

            if value >= minimum:
                return value

        print(f"Enter a whole number of at least {minimum}.")


def create_hero():
    """Ask for character information and create a hero."""
    name = input("Character name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Character name: ").strip()

    character_class = input(
        "Class (Warrior / Mage / Ranger, Enter = Warrior): "
    ).strip().title()

    if not character_class:
        return create_character(name)

    while character_class not in ("Warrior", "Mage", "Ranger"):
        print("Unknown class. Choose Warrior, Mage or Ranger.")
        character_class = input("Class: ").strip().title()

    return create_character(
        name=name,
        character_class=character_class
    )


def add_inventory_item(character):
    """Ask for item information and add it to inventory."""
    name = input("Item name: ").strip()

    while not name:
        print("Item name cannot be empty.")
        name = input("Item name: ").strip()

    item_type = input(
        "Item type (weapon / consumable / misc): "
    ).strip().lower()

    if not item_type:
        item_type = "misc"

    bonus = ask_for_integer("Bonus (0 if none): ", minimum=0)

    result = add_item(character, name, item_type, bonus)

    if result is not None:
        print(f"{name} added to inventory.")


def remove_inventory_item(character):
    """Ask for an item name and remove it from inventory."""
    name = input("Name of the item to remove: ").strip()

    if remove_item(character, name):
        print("Item removed.")
    else:
        print("That item is not in the inventory.")


def main():
    """Run the RPG Character Manager application."""
    character = None

    while True:
        print("\n===== RPG CHARACTER MANAGER =====")
        print("1. Create character")
        print("2. Add inventory item")
        print("3. Remove inventory item")
        print("4. Level up")
        print("5. Show character sheet")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            character = create_hero()

            print(
                f"Welcome, {character['name']} "
                f"the {character['class']}!"
            )

        elif choice in ("2", "3", "4", "5"):

            if character is None:
                print("Create a character first (option 1).")
                continue

            if choice == "2":
                add_inventory_item(character)

            elif choice == "3":
                remove_inventory_item(character)

            elif choice == "4":
                new_level = level_up(character)
                print(
                    f"{character['name']} reached level {new_level}!"
                )

            elif choice == "5":
                show_character_sheet(character)

        elif choice == "0":
            print("Thanks for playing. Goodbye!")
            break

        else:
            print("Invalid option. Choose a number from 0 to 5.")


if __name__ == "__main__":
    main()
