def calculate_stats(hero_class, level):
    base_stats = {
        "Warrior": {"hp": 12, "atk": 5, "def": 6},
        "Mage": {"hp": 8, "atk": 8, "def": 3},
        "Rogue": {"hp": 10, "atk": 6, "def": 4}
    }
    
    stats = base_stats.get(hero_class, base_stats["Warrior"])
    
    return {
        "hp": stats["hp"] * level,
        "attack": stats["atk"] * level,
        "defense": stats["def"] * level
    }

def create_hero():
    print("\n--- Create a New Hero ---")
    name = input("Enter hero name: ").strip()
    
    print("Available classes: Warrior, Mage, Rogue")
    hero_class = input("Choose character class: ").strip().capitalize()
    if hero_class not in ["Warrior", "Mage", "Rogue"]:
        hero_class = "Warrior"
        print("Invalid class. Defaulted to Warrior.")
        
    level = 1
    stats = calculate_stats(hero_class, level)
    
    return {
        "name": name,
        "class": hero_class,
        "level": level,
        "hp": stats["hp"],
        "attack": stats["attack"],
        "defense": stats["defense"],
        "inventory": []
    }

def display_character_sheet(hero):
    if not hero:
        print("\nNo hero registered yet!")
        return
        
    print("\n==============================")
    print("       CHARACTER SHEET        ")
    print("==============================")
    print(f"Name:    {hero['name']}")
    print(f"Class:   {hero['class']}")
    print(f"Level:   {hero['level']}")
    print("------------------------------")
    print(f"HP:      {hero['hp']}")
    print(f"Attack:  {hero['attack']}")
    print(f"Defense: {hero['defense']}")
    print("------------------------------")
    items = ", ".join(hero['inventory']) if hero['inventory'] else "Empty"
    print(f"Inventory: {items}")
    print("==============================\n")

def add_item(hero):
    if not hero:
        print("\nCreate a hero first!")
        return
    item = input("Enter item name to add: ").strip()
    if item:
        hero["inventory"].append(item)
        print(f"[{item}] added to inventory.")

def remove_item(hero):
    if not hero:
        print("\nCreate a hero first!")
        return
    if not hero["inventory"]:
        print("Inventory is already empty.")
        return
        
    item = input("Enter item name to remove: ").strip()
    if item in hero["inventory"]:
        hero["inventory"].remove(item)
        print(f"[{item}] removed from inventory.")
    else:
        print(f"Item [{item}] not found in inventory.")

def level_up(hero):
    if not hero:
        print("\nCreate a hero first!")
        return
    hero["level"] += 1
    new_stats = calculate_stats(hero["class"], hero["level"])
    
    hero["hp"] = new_stats["hp"]
    hero["attack"] = new_stats["attack"]
    hero["defense"] = new_stats["defense"]
    
    print(f"\nLevel Up! {hero['name']} reached level {hero['level']}!")

def main():
    current_hero = None
    
    while True:
        print("=== Adventurers' Guild Character Manager ===")
        print("1. Register New Hero")
        print("2. Display Character Sheet")
        print("3. Add Item to Inventory")
        print("4. Remove Item from Inventory")
        print("5. Level Up")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            current_hero = create_hero()
            print(f"\nHero {current_hero['name']} successfully registered!")
        elif choice == "2":
            display_character_sheet(current_hero)
        elif choice == "3":
            add_item(current_hero)
        elif choice == "4":
            remove_item(current_hero)
        elif choice == "5":
            level_up(current_hero)
        elif choice == "6":
            print("\nLeaving the Adventurers' Guild. Goodbye!")
            break
        else:
            print("\nInvalid selection. Please try again.\n")

if __name__ == "__main__":
    main()
