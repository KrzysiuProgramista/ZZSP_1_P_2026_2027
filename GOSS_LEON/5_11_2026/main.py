from character import create_character, calculate_stats, level_up
from inventory import add_item, remove_item


def show_character_sheet(character):
    hp, attack, defense = calculate_stats(character)

    print("\n" + "=" * 36)
    print("       CHARACTER SHEET")
    print("=" * 36)

    print(f"Class:   {character['class']}")
    print(f"Level:   {character['level']}")
    print(f"Name:    {character['name']}")



    print(f"Attack:  {attack}")
    print(f"Defense: {defense}")
    print("-" * 36)
    print(f"HP:      {hp}")

    print("-" * 36)
    print("Inventory:")

    if character["inventory"]:
        for number, item in enumerate(character["inventory"], start=1):
            print(
                f"{number}. {item['name']} "
                f"({item['type']}, bonus: {item['bonus']})"
            )
    else:
        print("your inventory is empty.")

    print("=" * 36)


def ask_for_integer(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt))

            if value >= minimum:
                return value

            print(f"enter a number of at least {minimum}.")

        except ValueError:
            print("please enter a whole number.")


def create_hero():
    name = input("character name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("character name: ").strip()

    character_class = input(
        "Class (warrior / mage / ranger, Enter = varrior): "
    ).strip().title()

    if not character_class:
        return create_character(name)

    while character_class not in ("warrior", "mage", "ranger"):
        print("unknown class. choose warrior, mage or ranger.")
        character_class = input("Class: ").strip().title()

    return create_character(
        name=name,
        character_class=character_class
    )


def add_inventory_item(character):
    name = input("item name: ").strip()

    while not name:
        print("item name cannot be empty.")
        name = input("Item name: ").strip()

    item_type = input(
        "item type (weapon / consumable / misc): "
    ).strip().lower()

    if not item_type:
        item_type = "misc"

    bonus = ask_for_integer("bonus (0 if none): ", minimum=0)

    try:
        add_item(character, name, item_type, bonus)
        print(f"{name} added to inventory.")

    except ValueError as error:
        print(error)


def remove_inventory_item(character):

    name = input("name of the item to remove: ").strip()

    if remove_item(character, name):
        print("item removed.")
    else:
        print("that item is not in the inventory.")


def main():

    character = None

    while True:
        print("\n===== RPG CHARACTER MANAGER =====")
        print("1. create character")
        print("2. add inventory item")
        print("3. remove inventory item")
        print("4. level up")
        print("5. show character sheet")
        print("0. exit")

        choice = input("choose an option: ").strip()

        if choice == "1":
            character = create_hero()

            print(
                f"welcome, {character['name']} "
                f"the {character['class']}!"
            )

        elif choice in ("2", "3", "4", "5"):

            if character is None:
                print("create a character first (option 1).")
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
            print("thanks for playing. Goodbye!")
            break

        else:
            print("invalid option. Choose a number from 0 to 5.")


if __name__ == "__main__":
    main()
