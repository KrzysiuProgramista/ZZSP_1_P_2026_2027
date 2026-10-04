print("Choose Rock/Paper/Scissors")

player_1 = input("Player 1 is choosing")
player_2 = input("Player 2 is choosing")

if player_1 == player_2:
    print("tie")
elif player_1 == "rock" and player_2 == "scissors":
    print("Player 1 Won")
elif player_1 == "paper" and player_2 == "rock":
    print("Player 1 Won")
elif player_1 == "scissors" and player_2 == "paper":
    print("Player 1 Won")
elif player_2 == "rock" and player_1 == "scissors":
    print("Player 2 Won")
elif player_2 == "paper" and player_1 == "rock":
    print("Player 2 Won")
elif player_2 == "scissors" and player_1 == "paper":
    print("Player 2 Won")
else:
    print("Error")
