
"""ESCAPE THE TEMPLE II: THE INNER SANCTUM"""

STARTING_ENERGY = 20
CRYSTAL_POWERS = [3, 8, 5, 2]
REQUIRED_ARTIFACTS = ["Bronze Key", "Sun Crystal", "Temple Seal"]

ROOMS = {
    "1": {
        "id": "library",
        "name": "The Forgotten Library",
        "distance": 2,
        "difficulty": 1,
        "requires": [],
        "artifact": "Bronze Key"
    },
    "2": {
        "id": "crystal",
        "name": "The Crystal Chamber",
        "distance": 2,
        "difficulty": 2,
        "requires": ["Bronze Key"],
        "artifact": "Sun Crystal"
    },
    "3": {
        "id": "bridge",
        "name": "The Broken Bridge",
        "distance": 3,
        "difficulty": 2,
        "requires": ["Bronze Key", "Sun Crystal"],
        "artifact": "Temple Seal"
    },
}


def show_status(inventory, energy):
    print("\n=== PLAYER STATUS ===")
    print("Energy:", energy)
    print("Artifacts:", inventory if inventory else "None collected")


def calculate_energy_cost(distance, difficulty):
    return distance * difficulty


def can_enter_room(room, inventory, energy, completed_rooms):
    if room["id"] in completed_rooms:
        return False

    for artifact in room["requires"]:
        if artifact not in inventory:
            return False

    cost = calculate_energy_cost(room["distance"], room["difficulty"])

    if energy < cost:
        return False

    return True


def sum_odd_crystals(values):
    total = 0

    for value in values:
        if value % 2 != 0:
            total += value

    return total


def is_palindrome(text):
    cleaned = ""

    for character in text.lower():
        if character.isalnum():
            cleaned += character

    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False

        left += 1
        right -= 1

    return len(cleaned) >= 3


def solve_puzzle(puzzle_id, answer):
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

    return False


def update_inventory(inventory, artifact):
    if artifact not in inventory:
        inventory.append(artifact)

    return inventory


def is_final_gate_unlocked(inventory):
    for artifact in REQUIRED_ARTIFACTS:
        if artifact not in inventory:
            return False

    return True


def room_clue(room_id):
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

    print("\n========================================")
    print(" ESCAPE THE TEMPLE II: THE INNER SANCTUM")
    print("========================================")
    print("You must collect 3 artifacts to escape!")

    while True:
        if energy <= 0 and not is_final_gate_unlocked(inventory):
            print("\nYou have run out of energy!")
            print("The temple remains locked. Game over.")
            break

        print("\n========== MAIN MENU ==========")
        print("1 - The Forgotten Library")
        print("2 - The Crystal Chamber")
        print("3 - The Broken Bridge")
        print("4 - Show status")
        print("5 - Try the final gate")
        print("6 - Quit")
        print("Energy:", energy)

        choice = input("Choose an option: ").strip()

        if choice == "6":
            print("You left the temple. Goodbye!")
            break

        elif choice == "4":
            show_status(inventory, energy)

        elif choice == "5":
            if is_final_gate_unlocked(inventory):
                print("\nThe final gate opens!")
                print("Congratulations! You escaped the temple!")
                break
            else:
                print("\nThe gate is locked!")
                print("You still need:")
                for artifact in REQUIRED_ARTIFACTS:
                    if artifact not in inventory:
                        print("-", artifact)

        elif choice in ROOMS:
            room = ROOMS[choice]

            if not can_enter_room(
                room, inventory, energy, completed_rooms
            ):
                if room["id"] in completed_rooms:
                    print("You have already completed this room.")
                else:
                    missing = [
                        item for item in room["requires"]
                        if item not in inventory
                    ]

                    if missing:
                        print("You cannot enter yet. Missing:", missing)
                    else:
                        print("Not enough energy to enter this room.")
                continue

            cost = calculate_energy_cost(
                room["distance"], room["difficulty"]
            )

            energy -= cost

            print("\nYou enter:", room["name"])
            print("Energy used:", cost)
            print("Energy remaining:", energy)
            print("\nPuzzle:")
            print(room_clue(room["id"]))

            answer = input("Your answer: ")

            if solve_puzzle(room["id"], answer):
                print("\nCorrect! You solved the puzzle!")
                update_inventory(inventory, room["artifact"])
                completed_rooms.append(room["id"])
                print("Artifact collected:", room["artifact"])
            else:
                print("\nIncorrect answer!")
                print("You did not collect the artifact.")

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

    print("\n========== GAME SUMMARY ==========")
    show_status(inventory, energy)


if __name__ == "__main__":
    main()
