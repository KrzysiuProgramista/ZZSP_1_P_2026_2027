player1 = input("Choose: Rock,Paper,Scissors(all letters should be in lowercase): ")
player2 = input("Choose: Rock,Paper,Scissors(all letters should be in lowercase): ")

if player1 == "scissors" and player2 == "paper" or player1 == "rock" and player2 == "scissors" or player1 == "paper" and player2 == "rock":
    print("Player 1 wins")
#elif player1 == "rock" and player2 == "scissors":
    #print("Player 1 wins")
#elif player1 == "paper" and player2 == "rock":
    #print("Player 1 wins")

elif player2 == "scissors" and player1 == "paper" or player2 == "rock" and player1 == "scissors" or player2 == "paper" and player1 =="rock":
    print("Player2 Wins")

elif player1 == player2:
    print("Its a draw.")
else:
    print("Invalid choice.")