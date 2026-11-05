

from character import create_character, calculate_stats, level_up
from inventory import add_item, remove_item


def display_character(character):
    hp, attack, defense = calculate_stats(character)

    print("\n" + "=" * 36)
    print("        character information")
    print("=" * 36)

    print(f"name:    {character['name']}")
    print(f"class:   {character['class']}")
    print(f"level:   {character['level']}")
    print(f"attack:  {attack}")
    print(f"defense: {defense}")

    print("-" * 36)
    print(f"health:  {hp}")
    print("-" * 36)

    print("inventory:")

    if len(character["inventory"]) > 0:
        for i, item in enumerate(character["inventory"], 1):
            print(
                f"{i}. {item['name']} "
                f"({item['type']}, bonus: {item['bonus']})"
            )
    else:
        print("your inventory is empty.")

    print("=" * 36)


def get_number(message, minimum=0):
    while True:
        try:
            number = int(input(message))

            if number < minimum:
                print(f"enter a value greater than or equal to {minimum}.")
            else:
                return number

        except ValueError:
            print("please enter a valid whole number.")


def new_character():
    name = input("enter character name: ").strip()

    while len(name) == 0:
        print("name cannot be empty.")
        name = input("enter character name: ").strip()

    char_class = input(
        "choose class (warrior / mage / ranger, enter = warrior): "
    ).strip().lower()

    if char_class == "":
        return create_character(name)

    while char_class not in ["warrior", "mage", "ranger"]:
        print("this class does not exist.")
        char_class = input("choose your class: ").strip().lower()

    return create_character(
        name=name,
        character_class=char_class
    )


def put_item_in_inventory(character):
    item_name = input("enter item name: ").strip()

    while not item_name:
        print("item name cannot be empty.")
        item_name = input("enter item name: ").strip()

    category = input(
        "item category (weapon / consumable / misc): "
    ).strip().lower()

    if category == "":
        category = "misc"

    item_bonus = get_number("enter item bonus: ")

    try:
        add_item(character, item_name, category, item_bonus)
        print(f"{item_name} was added successfully.")

    except ValueError as error:
        print(error)


def delete_item(character):
    item_name = input("enter the name of the item: ").strip()

    removed = remove_item(character, item_name)

    if removed:
        print("item successfully removed.")
    else:
        print("item not found.")


def main():
    hero = None

    while True:
        print("\n===== character manager =====")
        print("1. create a new character")
        print("2. add an item")
        print("3. delete an item")
        print("4. increase level")
        print("5. display character")
        print("0. quit")

        option = input("select an option: ").strip()

        if option == "1":
            hero = new_character()

            print(
                f"welcome {hero['name']}, "
                f"your class is {hero['class']}!"
            )

        elif option in ["2", "3", "4", "5"]:

            if hero is None:
                print("you need to create a character first.")
                continue

            if option == "2":
                put_item_in_inventory(hero)

            elif option == "3":
                delete_item(hero)

            elif option == "4":
                level = level_up(hero)
                print(f"you reached level {level}!")

            elif option == "5":
                display_character(hero)

        elif option == "0":
            print("thanks for playing. goodbye!")
            break

        else:
            print("wrong option. choose a number between 0 and 5.")


if __name__ == "__main__":
    main()
