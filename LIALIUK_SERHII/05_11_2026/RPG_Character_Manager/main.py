from character import BASE_STATS,DEFAULT_LEVEL,create_character,calculate_stats,level_up
from inventory import add_item,remove_item

def show_character_sheet(character):
    hp,attack,defense = calculate_stats(character)
    print("")
    print("\n>>>> Character <<<<")
    print("Name: ", character["name"])
    print("Class: ", character["class"])
    print("Level: ", character["level"])

    print("\n------- Stats --------")
    print("HP: ", hp)
    print("Attack: ", attack)
    print("Defense: ", defense)

    print('\n------- Inventory ------')

    if len(character["inventory"]) == 0:
        print("(nothing there...)")
    else:
        for item in character["inventory"]:
            print(
                "--->", item["name"], "| type:", item["type"], "| bonus:", item["bonus"]
                )
        print('-------------------------------------')

def get_input(prompt, result=None):
    while True:
        value=input(prompt)
        if value == "":
            return result
        try:
            return int(value)
        except ValueError:
            print("Enter a valid number,not something else.")
def main():
    """Run the Main program"""
    character=None
    while True:
        print('\n ------- Main Menu -------')
        print("1. Create character")
        print("2. Add inventory item")
        print("3. Remove inventory item")
        print("4. Level Up")
        print('5. Show Character Sheet')
        print("0. Exit")
        Main_input = input("\n Print the any of these number to proceed: ")
        if Main_input == "0":
            print("See you next time!")
            break
        elif Main_input == "1":
            name = input("Enter the name of your future character!: ")
            while not name.strip():
                print("Do you really wanna be nameless?: ")
                Nameless_Input= input("Print Y or N: ")
                if Nameless_Input.lower() == "y":
                    print("Okay,that's your wish i guess.")
                    Nameless = "??????????"
                    name = Nameless
                    break
                elif Nameless_Input.lower() == "n":
                    print("Lets try again!")
                    name = input("Enter the name of your future character!: ")
                else:
                    print("Invalid answer")
                    name = input("Enter the name of your future character!: ")
            print("\n Choose the avaliable class")
            print(
                "\n1.Warrior"
                "\n2.Mage"
                "\n3.Ranger"
            )

            character_class = input(
                "For choosing a class,enter the numbers!(If you don't,defualt class is Warrior): "
            )
            if character_class == "":
                character_class = "Warrior"
            elif character_class not in ('1','2','3'):
                print("Invalid choice,please type the correct number")
                character_class = input(
                            "For choosing a class,enter the numbers!(If you don't,defualt class is Warrior):"
                )
                continue

            if character_class == "1":
                character_class = "Warrior"
            elif character_class == "2":
                character_class = "Mage"
            elif character_class == "3":
                character_class = "Ranger"
            level = get_input(
                "Enter level!(Defualt is set as 1): ", DEFAULT_LEVEL
            )
            if level < 1:
                print("Level must be as 1,not lower.")    
                continue
            character = create_character(
                name=name,
                character_class=character_class,
                level=level
            )
            print("Character successfully created!")
        elif Main_input == "2":
            if character is None:
                print("Without a character you can't do it! First,Create a character!")
                continue
            item_name = input("Enter how your item will be called!:  ")
            if not item_name.strip():
                print("Item name cannot be empty you know!")
                continue
            item_type = input(
                "Enter the item type!(Defualt will be misc): "
            )
            if item_type == "":
                    item_type = "misc"
            bonus = get_input(
                "Enter bonus for your future item! (defualt 0): ", 0
                )
            add_item(character,item_name,item_type,bonus)
            print("Item successfully have been added!")
        elif Main_input == "3":
            if character is None:
                print("Without a character you can't do it! First,Create a character!")
                continue
            item_name = input("Enter the name of the item to remove it!: ")
            if remove_item(character,item_name):
                print("Item successfully removed!")
            else:
                print("Im sorry but item haven't been found :(")
        elif Main_input == "4":
            if character is None:
                print("Without a character you can't do it! First,Create a character!")
                continue
            level_up(character)
            print(
                "You just leveled up! Your current level is: "
                f"{character['level']} "
            )
        elif Main_input == "5":
            if character is None:
                print("Without a character you can't do it! First,Create a character!")
                continue
            show_character_sheet(character)
        else:
            print("Invalid Menu Key,im sorry! :(")
if __name__ == "__main__":
    main()