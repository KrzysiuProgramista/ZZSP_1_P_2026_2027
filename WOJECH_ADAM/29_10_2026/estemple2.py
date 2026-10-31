STARTING_ENERGY = 20
CRYSTAL_POWERS = [3, 8, 5, 2]
REQUIRED_ARTIFACTS = ["Bronze Key", "Sun Crystal", "Temple Seal"]

ROOMS = {
    "1": {"id": "library", "name": "The Forgotten Library", "distance": 2,
          "difficulty": 1, "requires": [], "artifact": "Bronze Key"},
    "2": {"id": "crystal", "name": "The Crystal Chamber", "distance": 2,
          "difficulty": 2, "requires": ["Bronze Key"], "artifact": "Sun Crystal"},
    "3": {"id": "bridge", "name": "The Broken Bridge", "distance": 3,
          "difficulty": 2, "requires": ["Bronze Key", "Sun Crystal"], "artifact": "Temple Seal"},
}


def show_status(inventory, energy):
    """Print current energy and collected artifacts."""
    print("\n--- STATUS ---")
    print(f"Energy: {energy}")
    if inventory:
        print("Artifacts: " + ", ".join(inventory))
    else:
        print("Artifacts: None")
    print("-"*14)


def calculate_energy_cost(distance, difficulty):
    """Return the energy cost: distance multiplied by difficulty."""
    return distance * difficulty


def can_enter_room(room, inventory, energy, completed_rooms):
    """Return True if this room is available and affordable."""
    if room["id"] in completed_rooms:
        return False  
    for required_artifact in room["requires"]:
        if required_artifact not in inventory:
            return False
    cost = calculate_energy_cost(room["distance"], room["difficulty"])
    if energy < cost:
        return False
    return True


def sum_odd_crystals(values):
    """Return the sum of odd numbers in values, using a loop."""
    total = 0
    for value in values:
        if value % 2 != 0:
            total += value
    return total


def is_palindrome(text):
    """Return True when text is a palindrome, ignoring case and spaces/punctuation."""
    cleaned = ""
    for char in text.lower():
        if char.isalnum():
            cleaned += char
    left = 0
    right = len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
        
    return True


def solve_puzzle(puzzle_id, answer):
    """Return True if the answer solves the requested room's puzzle."""
    normalized = answer.strip().lower()
    if puzzle_id == "library":
        return normalized == "echo"
    elif puzzle_id == "crystal":
        try:
            return int(normalized) == sum_odd_crystals(CRYSTAL_POWERS)
        except ValueError:
            return False
    elif puzzle_id == "bridge":
        letter_count = sum(1 for char in normalized if char.isalpha())
        if letter_count < 3:
            return False
        return is_palindrome(normalized)
    return False


def update_inventory(inventory, artifact):
    """Add artifact if it is not already present; return inventory."""
    if artifact not in inventory:
        inventory.append(artifact)
    return inventory


def is_final_gate_unlocked(inventory):
    """Return True only if all REQUIRED_ARTIFACTS are in inventory."""
    for artifact in REQUIRED_ARTIFACTS:
        if artifact not in inventory:
            return False
    return True


def room_clue(room_id):
    """Return the room's puzzle clue as a string."""
    if room_id == "library":
        return "I speak without a mouth and hear without ears. What am I?"
    if room_id == "crystal":
        return "Add only the ODD crystal powers: [3, 8, 5, 2]. What is the total?"
    if room_id == "bridge":
        return "Enter a palindrome with at least 3 letters. Ignore spaces and case."
    return "Unknown room."


def main():
    inventory = []
    completed_rooms = []
    energy = STARTING_ENERGY

    print("=" *45)
    print("   ESCAPE THE TEMPLE II: THE INNER SANCTUM   ")
    print("=" *45)
    while True:
        print("\n--- MAIN MENU ---")
        print("1 - Enter The Forgotten Library")
        print("2 - Enter The Crystal Chamber")
        print("3 - Enter The Broken Bridge")
        print("4 - Check Status")
        print("5 - Try Final Gate")
        print("6 - Quit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice in ["1", "2", "3"]:
            room = ROOMS[choice]
            if not can_enter_room(room, inventory, energy, completed_rooms):
                print(f"\nYou cannot enter {room['name']} right now.")
                print("(Either you lack the required artifacts, it's already completed, or you don't have enough energy).")
                continue
            cost = calculate_energy_cost(room["distance"], room["difficulty"])
            energy -= cost
            print(f"\nYou enter {room['name']}. (Energy -{cost}, Remaining: {energy})")
            print(f"Clue: {room_clue(room['id'])}")
            answer = input("Your answer: ")
            if solve_puzzle(room["id"], answer):
                print("\nCorrect! You solved the puzzle.")
                update_inventory(inventory, room["artifact"])
                completed_rooms.append(room["id"])
                print(f"You obtained: {room['artifact']}!")
            else:
                print("\nIncorrect answer. The temple consumes your energy, but the room remains unsolved.")
                
        elif choice == "4":
            show_status(inventory, energy)
            
        elif choice == "5":
            print("\nYou approach the Guardian's Altar...")
            if is_final_gate_unlocked(inventory):
                print("You place all three artifacts into the altar.")
                print("The massive stone doors grind open. You have escaped the Inner Sanctum!")
                print("YOU WIN!")
                break
            else:
                print("The altar remains dark. You need all three artifacts to unlock it.")
                
        elif choice == "6":
            print("\nYou decide to give up and leave the temple. Game Over.")
            break
            
        else:
            print("\nInvalid choice. Please select a number between 1 and 6.")
        if energy <= 0 and not is_final_gate_unlocked(inventory):
            print("\nYou have run out of energy The temple traps you forever.")
            print("GAME OVER")
            break


if __name__ == "__main__":
    main()