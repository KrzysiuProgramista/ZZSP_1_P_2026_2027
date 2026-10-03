rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

p1 = input("P1: ").strip().lower()
p2 = input("P2: ").strip().lower()

if p1 not in rules or p2 not in rules:
    print("Error: Invalid choice entered.")
elif p1 == p2:
    print("It's a draw!")
else:
    if rules[p1] == p2:
        print("Player 1 won.")
    else:
        print("Player 2 won.")
