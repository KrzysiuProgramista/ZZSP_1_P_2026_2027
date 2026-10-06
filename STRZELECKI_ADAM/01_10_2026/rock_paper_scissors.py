print("Rock, Paper, Scissors")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

choice1 = int(input("Player 1, enter your choice (1,2 or 3): "))
choice2 = int(input("Player 2, enter your choice (1,2 or 3): "))
if (choice1 or choice2) not in [1,2,3]:
    print("Your choice is invalid.")

if (choice1 == 1 and choice2 == 1) or (choice1 == 2 and choice2 == 2) or (choice1 == 3 and choice2 == 3):
    print("Draw!")
elif (choice1 == 1 and choice2 == 2) or (choice1 == 2 and choice2 == 3) or (choice1 == 3 and choice2 == 1):
    print("Player 2 wins!")
elif (choice1 == 1 and choice2 == 3) or (choice1 == 2 and choice2 == 1) or (choice1 == 3 and choice2 == 2):
    print("Player 1 wins!")
