

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
    """Print current energy and collected artifacts."""
    print("\n--- PLAYER STATUS ---")
    print(f"Energy: {energy}")
    print("Artifacts:")

    if inventory:
        for artifact in inventory:
            print(f"- {artifact}")
    else:
        print("- None")

    print()


def calculate_energy_cost(distance, difficulty):
    """Return the energy cost."""
    return distance * difficulty


def can_enter_room(room, inventory, energy, completed_rooms):
    """Return True if the room is available and affordable."""
    if room["id"] in completed_rooms:
        return False

    for artifact in room["requires"]:
        if artifact not in inventory:
            return False

    cost = calculate_energy_cost(
        room["distance"],
        room["difficulty"]
    )

    return energy >= cost


def sum_odd_crystals(values):
    """Return the sum of odd numbers using a loop."""
    total = 0

    for value in values:
        if value % 2 != 0:
            total += value

    return total


def is_palindrome(text):
    """Check a palindrome, ignoring case, spaces and punctuation."""
    normalized = ""

    for character in text.lower():
        if character.isalnum():
            normalized += character

    left = 0
    right = len(normalized) - 1

    while left < right:
        if normalized[left] != normalized[right]:
            return False

        left += 1
        right -= 1

    return True


def solve_puzzle(puzzle_id, answer):
    """Return True if the answer solves the puzzle."""
    normalized = answer.strip().lower()

    if puzzle_id == "library":
        return normalized == "echo"

    if puzzle_id == "crystal":
        try:
            return int(normalized) == sum_odd_crystals(CRYSTAL_POWERS)
        except ValueError:
            return False

    if puzzle_id == "bridge":
        return is_palindrome(answer) and sum(
            1 for character in answer if character.isalnum()
        ) >= 3

    return False


def update_inventory(inventory, artifact):
    """Add an artifact without duplicates."""
    if artifact not in inventory:
        inventory.append(artifact)

    return inventory


def is_final_gate_unlocked(inventory):
    """Check whether every required artifact has been collected."""
    for artifact in REQUIRED_ARTIFACTS:
        if artifact not in inventory:
            return False

    return True


def room_clue(room_id):
    """Return the room's puzzle clue."""
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

    print("=" * 48)
    print("ESCAPE THE TEMPLE II: THE INNER SANCTUM")
    print("=" * 48)
    print("You are trapped inside an ancient temple.")
    print("Collect all three artifacts to unlock the final gate.")
    print("Choose your moves carefully. Energy is limited.")

    while True:
        if energy <= 0 and not is_final_gate_unlocked(inventory):
            print("\nYou have run out of energy!")
            print("The temple seals itself forever. GAME OVER.")
            break

        print("\n========== TEMPLE MENU ==========")
        print("1 - The Forgotten Library")
        print("2 - The Crystal Chamber")
        print("3 - The Broken Bridge")
        print("4 - Show status")
        print("5 - Try the final gate")
        print("6 - Quit")
        print("=================================")

        choice = input("Choose an option: ").strip()

        if choice in ("1", "2", "3"):
            room = ROOMS[choice]

            if room["id"] in completed_rooms:
                print("\nYou have already completed this room.")
                continue

            if not can_enter_room(
                room, inventory, energy, completed_rooms
            ):
                missing = [
                    artifact for artifact in room["requires"]
                    if artifact not in inventory
                ]

                if missing:
                    print("\nYou cannot enter this room yet.")
                    print("Missing artifacts:", ", ".join(missing))
                else:
                    cost = calculate_energy_cost(
                        room["distance"], room["difficulty"]
                    )
                    print(f"\nNot enough energy! You need {cost} energy.")

                continue

            cost = calculate_energy_cost(
                room["distance"], room["difficulty"]
            )

            energy -= cost

            print(f"\nEntering: {room['name']}")
            print(f"Energy spent: {cost}")
            print(f"Energy remaining: {energy}")
            print("\nPUZZLE:")
            print(room_clue(room["id"]))

            answer = input("\nYour answer: ")

            if solve_puzzle(room["id"], answer):
                print("\nCorrect! You solved the puzzle.")

                artifact = room["artifact"]
                update_inventory(inventory, artifact)
                completed_rooms.append(room["id"])

                print(f"You collected: {artifact}")
            else:
                print("\nWrong answer!")
                print("You lost the energy required to enter the room.")

        elif choice == "4":
            show_status(inventory, energy)

        elif choice == "5":
            if is_final_gate_unlocked(inventory):
                print("\n" + "=" * 48)
                print("THE FINAL GATE OPENS!")
                print("You have collected every artifact.")
                print("You escape the temple victorious!")
                print("CONGRATULATIONS! YOU WIN!")
                print("=" * 48)
                break
            else:
                missing = [
                    artifact for artifact in REQUIRED_ARTIFACTS
                    if artifact not in inventory
                ]

                print("\nThe final gate remains locked.")
                print("You still need:")
                for artifact in missing:
                    print(f"- {artifact}")

        elif choice == "6":
            print("\nYou leave the temple behind. Goodbye!")
            break

        else:
            print("\nInvalid choice. Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
