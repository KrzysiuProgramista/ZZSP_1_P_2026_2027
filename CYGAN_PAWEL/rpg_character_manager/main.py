from character import create_character, calculate_stats, level_up
from inventory import add_item, remove_item

def show_character_sheet(character):
    """Display character information and current statistics."""
    hp, attack, defense = calculate_stats(character)
    print("\n========== CHARACTER SHEET ==========")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print("\n---------- STATISTICS ----------")
    print(f"HP: {hp}")
    print(f"Attack: {attack}")
    print(f"Defense: {defense}")
    print("\n---------- INVENTORY ----------")
    if not character["inventory"]:
        print("Inventory is empty.")
    else:
        for item in character["inventory"]:
            print(
                f"{item['name']} | "
                f"Type: {item['type']} | "
                f"Bonus: {item['bonus']}"
            )
    print("=====================================\n")
def get_integer(prompt, default=None):
    """Get a valid integer from the user."""
    while True:
        value = input(prompt)
        if value == "" and default is not None:
            return default
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.")
def main():
    """Run the RPG Character Manager application."""
    character = None
    while True:
        print("\n========== RPG CHARACTER MANAGER ==========")
        print("1. Create character")
        print("2. Add inventory item")
        print("3. Remove inventory item")
        print("4. Level up")
        print("5. Show character sheet")
        print("0. Exit")
        choice = input("\nChoose an option: ")
        if choice == "0":
            print("Goodbye, adventurer!")
            break
        elif choice == "1":
            name = input("Enter character name: ")
            while not name.strip():
                print("Name cannot be empty.")
                name = input("Enter character name: ")
            print("\nAvailable classes:")
            print("Warrior")
            print("Mage")
            print("Ranger")
            character_class = input(
                "Choose class (default Warrior): "
            )
            if character_class == "":
                character_class = "Warrior"
            if character_class not in ("Warrior", "Mage", "Ranger"):
                print("Invalid character class.")
                continue
            level = get_integer(
                "Enter level (default 1): ",
                DEFAULT_LEVEL
            )
            if level < 1:
                print("Level must be at least 1.")
                continue
            character = create_character(
                name=name,
                character_class=character_class,
                level=level
            )
            print("Character successfully created!")
        elif choice in ("2", "3", "4", "5"):
            if character is None:
                print("Create a character first!")
                continue
            if choice == "2":
                item_name = input("Enter item name: ")
                if not item_name.strip():
                    print("Item name cannot be empty.")
                    continue
                item_type = input(
                    "Enter item type (default misc): "
                )
                if item_type == "":
                    item_type = "misc"
                bonus = get_integer(
                    "Enter item bonus (default 0): ",
                    0
                )
                add_item(
                    character,
                    item_name,
                    item_type,
                    bonus
                )
                print("Item successfully added!")
            elif choice == "3":
                item_name = input("Enter item name to remove: ")
                if remove_item(character, item_name):
                    print("Item successfully removed!")
                else:
                    print("Item not found.")
            elif choice == "4":
                level_up(character)
                print(
                    f"Level up! Current level: "
                    f"{character['level']}"
                )
            elif choice == "5":
                show_character_sheet(character)
        else:
            print("Invalid menu option.")
if __name__ == "__main__":
    main()
