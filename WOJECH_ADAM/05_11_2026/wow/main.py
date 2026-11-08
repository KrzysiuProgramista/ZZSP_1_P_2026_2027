import json
import os
from character import create_character, calculate_stats, level_up, BASE_STATS
from inventory import add_item, remove_item
from battle import run_battle

SAVE_FILE = "characters.json"
DIVIDER = "=/_" * 20

def save_to_file(character_list):
#Save the list of characters to a JSON file
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(character_list, f, indent=4)
        print("[+] Progress saved to characters.json.")
    except Exception as e:
        print(f"[!] Failed to save characters: {e}")

def load_from_file():
#Load the list of characters from a JSON file
    if not os.path.exists(SAVE_FILE):
        return []
    try:
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Failed to load characters: {e}")
        return []

def show_character_sheet(character):
#Display the full character statistics and inventory details
    if not character:
        print("\n No active character. Please select or create one first!")
        return

    hp, attack, defense = calculate_stats(character)
    
    print(f"\n{DIVIDER}\n       CHARACTER SHEET        \n{DIVIDER}")
    print(f"Name:    {character['name']}")
    print(f"Class:   {character['class']}")
    print(f"Level:   {character['level']}\n{DIVIDER}")
    print(f"HP:      {hp} (Base + Potions)")
    print(f"Attack:  {attack} (Base + Weapons)")
    print(f"Defense: {defense} (Base + Armor)\n{DIVIDER}\nInventory:")
    
    if not character["inventory"]:
        print("  (Empty)")
    else:
        for item in character["inventory"]:
            print(f"  _ {item['name']} [{item['type'].upper()} Bonus: +{item['bonus']}]")
    print(f"{DIVIDER}\n")

def main():
#Run the main interactive menu for the character manager
    heroes_database = load_from_file()
    active_idx = 0 if heroes_database else None

    print("Welcome to the Ultimate Adventurers' Guild Hero Manager!")

    while True:
        active_hero = heroes_database[active_idx] if active_idx is not None and heroes_database else None
        
        print(f"{DIVIDER}\n--- STATUS ---")
        if active_hero:
            print(f"Active Hero: {active_hero['name']} the {active_hero['class']} (Lvl {active_hero['level']})")
        else:
            print("Active Hero: None (Please create or load a hero)")
        print(f"Total Registered Heroes: {len(heroes_database)}\n{DIVIDER}")
        
        print("1. Create new character\n2. Switch active character (Multiple Heroes)\n"
              "3. Add inventory item (Weapon/Armor/Potion)\n4. Remove inventory item\n"
              "5. Level up active hero\n6. Show active character sheet\n"
              "7. ENTER THE BATTLE SIMULATOR\n8. Save all characters to file\n0. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice in ["3", "4", "5", "6", "7"] and not active_hero:
            print("[!] Please select or create a character first!\n")
            continue

        if choice == "1":
            name = input("Enter character name: ").strip()
            if not name:
                print("[!] Error: Character name cannot be empty!\n")
                continue
                
            print(f"Available classes: {', '.join(BASE_STATS.keys())}")
            char_class = input("Enter class (Default 'Warrior'): ").strip().capitalize()
            
            if not char_class or char_class not in BASE_STATS:
                if char_class: 
                    print("[!] Error: Unknown class! Defaulting to Warrior.")
                char_class = "Warrior"
            
            new_hero = create_character(name=name, character_class=char_class, level=1)
            heroes_database.append(new_hero)
            active_idx = len(heroes_database) - 1
            print(f"[+] Character {name} created and set as active!\n")
            
        elif choice == "2":
            if not heroes_database:
                print("[!] No characters available to switch between!\n")
                continue
            print("\n--- Available Heroes ---")
            for idx, hero in enumerate(heroes_database):
                print(f"{idx}. {hero['name']} - {hero['class']} (Level {hero['level']})")
            
            try:
                sel = int(input("Select character index: "))
                if 0 <= sel < len(heroes_database):
                    active_idx = sel
                    print(f"[+] Switched to hero: {heroes_database[active_idx]['name']}\n")
                else:
                    print("[!] Index out of range!\n")
            except ValueError:
                print("[!] Invalid input number!\n")
                
        elif choice == "3":
            item_name = input("Enter item name: ").strip()
            if not item_name:
                print("[!] Item name cannot be empty!\n")
                continue
                
            print("Types: weapon (buffs ATK), armor (buffs DEF), potion (buffs HP), misc")
            item_type = input("Enter item type: ").strip().lower()
            if item_type not in ["weapon", "armor", "potion", "misc"]:
                item_type = "misc"
                
            try:
                bonus_input = input("Enter item bonus value: ").strip()
                item_bonus = int(bonus_input) if bonus_input else 0
            except ValueError:
                print("[!] Invalid number! Setting bonus to 0.")
                item_bonus = 0
                
            add_item(active_hero, item_name, item_type, item_bonus)
            print(f"[+] Added {item_name} to {active_hero['name']}'s inventory.\n")
            
        elif choice == "4":
            item_name = input("Enter item name to remove: ").strip()
            if remove_item(active_hero, item_name):
                print(f"[+] Successfully removed {item_name}.\n")
            else:
                print(f"[-] Item '{item_name}' not found!\n")
                
        elif choice == "5":
            level_up(active_hero)
            print(f"[+] Leveled up! Current Level: {active_hero['level']}\n")
            
        elif choice == "6":
            show_character_sheet(active_hero)
            
        elif choice == "7":
            run_battle(active_hero)
            
        elif choice == "8":
            save_to_file(heroes_database)
            
        elif choice == "0":
            save_to_file(heroes_database)
            print("Goodbye, ultimate hero!")
            break
        else:
            print("[!] Invalid choice!\n")

if __name__ == "__main__":
    main()
