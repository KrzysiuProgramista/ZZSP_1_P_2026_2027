player1 = input("Player 1 (rock/paper/scissors): ").lower()
player2 = input("Player 2 (rock/paper/scissors): ").lower()

choices = ["rock", "paper", "scissors"]

if player1 not in choices or player2 not in choices:
    print("Invalid choice!")
elif player1 == player2:
    print("It's a draw!")
elif (
    (player1 == "rock" and player2 == "scissors")
    or (player1 == "scissors" and player2 == "paper")
    or (player1 == "paper" and player2 == "rock")
):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")