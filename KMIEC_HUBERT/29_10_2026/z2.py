"""
ESCAPE THE TEMPLE II: THE INNER SANCTUM
Student starter code - COMPLETED WITH BONUS CHALLENGES.
"""

STARTING_ENERGY = 25  # Zwiększono lekko energię początkową z uwagi na dodatkowy pokój
CRYSTAL_POWERS = [3, 8, 5, 2]
REQUIRED_ARTIFACTS = ["Bronze Key", "Sun Crystal", "Temple Seal", "Sacred Idol"]

ROOMS = {
    "1": {"id": "library", "name": "The Forgotten Library", "distance": 2, "difficulty": 1, "requires": [], "artifact": "Bronze Key"},
    "2": {"id": "crystal", "name": "The Crystal Chamber", "distance": 2, "difficulty": 2, "requires": ["Bronze Key"], "artifact": "Sun Crystal"},
    "3": {"id": "bridge", "name": "The Broken Bridge", "distance": 3, "difficulty": 2, "requires": ["Bronze Key", "Sun Crystal"], "artifact": "Temple Seal"},
    "4": {"id": "vault", "name": "The Golden Vault", "distance": 2, "difficulty": 3, "requires": ["Temple Seal"], "artifact": "Sacred Idol"}
}

def show_status(inventory, energy):
    """Print current energy and collected artifacts."""
    print("\n--- STATUS ---")
    print(f"Energy: {energy}")
    if inventory:
        print(f"Inventory: {', '.join(inventory)}")
    else:
        print("Inventory: [Empty]")
    print("--------------")

def calculate_energy_cost(distance, difficulty):
    """Return the energy cost: distance multiplied by difficulty."""
    return distance * difficulty

def can_enter_room(room, inventory, energy, completed_rooms):
    """Return True if this room is available and affordable."""
    if room["id"] in completed_rooms:
        print("You have already completed this room!")
        return False
    
    for req in room["requires"]:
        if req not in inventory:
            print(f"Missing required artifact: {req}")
            return False
            
    cost = calculate_energy_cost(room["distance"], room["difficulty"])
    if energy < cost:
        print(f"Not enough energy! Requires {cost} energy, you have {energy}.")
        return False
    return True

def sum_odd_crystals(values):
    """Return the sum of odd numbers in values, using a loop."""
    total = 0
    for val in values:
        if val % 2 != 0:
            total += val
    return total

def is_palindrome(text):
    """Return True when text is a palindrome, ignoring case and spaces/punctuation."""
    cleaned = ""
    for char in text.lower():
        if char.isalnum():
            cleaned += char
            
    if len(cleaned) < 3:
        return False
        
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

def count_vowels(text):
    """BONUS D: Nowa funkcja pomocnicza zliczająca samogłoski w tekście."""
    vowels = "aeiouy"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

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
        return is_palindrome(answer)
    elif puzzle_id == "vault":
        try:
            # Prawidłowa odpowiedź dla słowa "SANCTUM" to 2 samogłoski (a, u)
            return int(normalized) == count_vowels("SANCTUM")
        except ValueError:
            return False
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
    elif room_id == "crystal":
        return "Add only the ODD crystal powers. What is the total?"
    elif room_id == "bridge":
        return "Enter a palindrome with at least 3 letters. Ignore spaces and case."
    elif room_id == "vault":
        return "BONUS PUZZLE: How many vowels are in the word 'SANCTUM'?"
    return "Unknown room."

def room_hint(room_id):
    """BONUS B: Zwraca podpowiedź po błędnej próbie."""
    if room_id == "library":
        return "Think of sound bouncing off walls in a cave."
    elif room_id == "crystal":
        return f"The crystal numbers are {CRYSTAL_POWERS}. Identify which are odd and add them."
    elif room_id == "bridge":
        return "Examples: 'kayak', 'radar', or 'racecar'."
    elif room_id == "vault":
        return "Vowels are A, E, I, O, U, Y. Look closely at S-A-N-C-T-U-M."
    return "No hint available."

def main():
    inventory = []
    completed_rooms = []
    energy = STARTING_ENERGY
    
    print("ESCAPE THE TEMPLE II: THE INNER SANCTUM (Enhanced Edition)")
    
    while True:
        print("\n=== MAIN MENU ===")
        print("1 - Library")
        print("2 - Crystal Chamber")
        print("3 - Broken Bridge")
        print("4 - Golden Vault (Bonus)")
        print("5 - Status")
        print("6 - Try final gate")
        print("7 - Quit")
        
        choice = input("Choose an option: ").strip()
        
        if choice in ["1", "2", "3", "4"]:
            room = ROOMS[choice]
            if can_enter_room(room, inventory, energy, completed_rooms):
                cost = calculate_energy_cost(room["distance"], room["difficulty"])
                energy -= cost
                print(f"\nYou enter {room['name']}. Energy spent: {cost}. Remaining energy: {energy}")
                
                # BONUS A: Limit do 3 prób na pokój
                attempts = 3
                success = False
                
                while attempts > 0:
                    print(f"\nClue: {room_clue(room['id'])}")
                    print(f"Attempts remaining: {attempts}")
                    answer = input("Your answer: ")
                    
                    if solve_puzzle(room['id'], answer):
                        print(f"Correct! You acquired the {room['artifact']}.")
                        inventory = update_inventory(inventory, room['artifact'])
                        completed_rooms.append(room['id'])
                        success = True
                        break
                    else:
                        attempts -= 1
                        if attempts > 0:
                            print("\nIncorrect answer!")
                            print(f"HINT: {room_hint(room['id'])}") # BONUS B: Podpowiedź
                        else:
                            print("\nIncorrect! You ran out of attempts for this entry.")
                
                if not success:
                    print("The room expels you. You can try entering again (costs energy!).")
                    
        elif choice == "5":
            show_status(inventory, energy)
            
        elif choice == "6":
            if is_final_gate_unlocked(inventory):
                print("\nCONGRATULATIONS! The Inner Sanctum opens. You have escaped the temple!")
                break
            else:
                print("\nThe final gate remains sealed. You are missing required artifacts.")
                print(f"Required: {', '.join(REQUIRED_ARTIFACTS)}")
                
        elif choice == "7":
            print("\nYou abandon the quest. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 7.")
            
        if energy <= 0 and not is_final_gate_unlocked(inventory):
            print("\nGAME OVER! Your energy is completely depleted and you cannot open the gate.")
            break

if __name__ == "__main__":
    main()
