"""ESCAPE THE TEMPLE II: THE INNER SANCTUM
Student starter code. Complete the TODOs in small steps.
Do not add external libraries. Use functions that RETURN values.
"""

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
    print("Energy:", energy)
    if inventory:
        print("Artifacts:", ", ".join(inventory))
    else:
        print("Artifacts: (none)")


def calculate_energy_cost(distance, difficulty):
    """Return the energy cost: distance multiplied by difficulty."""
    return distance * difficulty


def can_enter_room(room, inventory, energy, completed_rooms):
    """Return True if this room is available and affordable."""
    if room["id"] in completed_rooms:
        return False

    for artifact in room["requires"]:
        if artifact not in inventory:
            return False

    cost = calculate_energy_cost(room["distance"], room["difficulty"])
    return energy >= cost


def sum_odd_crystals(values):
    """Return the sum of odd numbers in values, using a loop."""
    total = 0
    for value in values:
        if value % 2 != 0:
            total += value
    return total


def is_palindrome(text):
    """Return True when text is a palindrome, ignoring case and spaces/punctuation."""
    normalized = ""
    for ch in text.lower():
        if ch.isalnum():
            normalized += ch

    left = 0
    right = len(normalized) - 1
    while left < right:
        if normalized[left] != normalized[right]:
            return False
        left += 1
        right -= 1
    return True


def solve_puzzle(puzzle_id, answer):
    """Return True if the answer solves the requested room's puzzle."""
    normalized = answer.strip().lower()

    if puzzle_id == "library":
        return normalized == "echo"

    if puzzle_id == "crystal":
        return normalized == str(sum_odd_crystals(CRYSTAL_POWERS))

    if puzzle_id == "bridge":
        cleaned = ""
        for ch in answer:
            if ch.isalnum():
                cleaned += ch.lower()
        return len(cleaned) >= 3 and is_palindrome(cleaned)

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

    print("ESCAPE THE TEMPLE II: THE INNER SANCTUM")

    while True:
        print()
        print("1 - The Forgotten Library")
        print("2 - The Crystal Chamber")
        print("3 - The Broken Bridge")
        print("4 - Status")
        print("5 - Try final gate")
        print("6 - Quit")

        choice = input("Choose an option: ").strip()

        if choice == "4":
            show_status(inventory, energy)

        elif choice == "5":
            if is_final_gate_unlocked(inventory):
                print("The great gate grinds open. YOU ESCAPED THE TEMPLE!")
                break
            still_needed = []
            for artifact in REQUIRED_ARTIFACTS:
                if artifact not in inventory:
                    still_needed.append(artifact)
            print("The gate is sealed. Still needed:", ", ".join(still_needed))

        elif choice == "6":
            print("You slip away into the jungle. Goodbye.")
            break

        elif choice in ROOMS:
            room = ROOMS[choice]

            if not can_enter_room(room, inventory, energy, completed_rooms):
                if room["id"] in completed_rooms:
                    print("You have already cleared this room.")
                else:
                    missing = []
                    for artifact in room["requires"]:
                        if artifact not in inventory:
                            missing.append(artifact)
                    if missing:
                        print("Locked! You still need:", ", ".join(missing))
                    else:
                        print("You are too tired to enter. Not enough energy.")
                continue

            cost = calculate_energy_cost(room["distance"], room["difficulty"])
            energy -= cost
            print(f"You enter {room['name']} and spend {cost} energy.")

            print("Puzzle:", room_clue(room["id"]))
            answer = input("Your answer: ")

            if solve_puzzle(room["id"], answer):
                print("Correct! You found:", room["artifact"])
                inventory = update_inventory(inventory, room["artifact"])
                completed_rooms.append(room["id"])
            else:
                print("Wrong... the room stays sealed, and your energy was spent.")

            if energy <= 0 and not is_final_gate_unlocked(inventory):
                print("Out of energy with the gate still sealed. GAME OVER.")
                break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
