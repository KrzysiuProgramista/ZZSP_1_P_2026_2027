player1 = (input("Player 1 please, enter rock, paper or scissors: "))
player2 = (input("Player 2 please, enter rock, paper or scissors: "))
if player1 in ("rock", "scissors", "paper") and player2 in ("rock", "scissors", "paper"):
    if (player1 == player2):
        print("Draw!")
    elif (player1 == "rock") & (player2 == "scissors"):
        print("Player 1 Won!")
    elif (player1 == "paper") & (player2 == "rock"):
        print("Player 1 Won!")
    elif (player1 == "scissors") & (player2 == "paper"):
        print("Player 1 Won!")
    elif (player2 == "rock") & (player1 == "scissors"):
        print("Player 2 Won!")
    elif (player2 == "paper") & (player1 == "rock"):
        print("Player 2 Won!")
    elif (player2 == "scissors") & (player1 == "paper"):
        print("Player 2 Won!")
else:
    print("Wrong choice!")
