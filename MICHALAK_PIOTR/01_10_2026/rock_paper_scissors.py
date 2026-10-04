right = ["rock","paper","scissors"]

player1 = input("Player 1: ")
player2 = input("Player 2: ")

if player1 in right and player2 in right:
    if (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins")
    elif player1 == player2:
        print("Tie")
    else:
        print("Player 2 wins")
else:
    print("Error: Invalid choice. Both players must choose rock, paper, or scissors.")