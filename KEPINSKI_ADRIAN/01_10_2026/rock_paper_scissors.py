player1name = input("Player 1 name: ")
player2name = input("Player 2 name: ")

player1 = input(f"{player1name}: rock, paper, scissors: ")
player2 = input(f"{player2name}: rock, paper, scissors: ")

plr1score = 0
plr2score = 0

if player1 == player2:
    print("It's a draw")
elif player1 == "rock" and player2 == "scissors":
    print(f"{player1name} wins")
    plr1score += 1
elif player1 == "paper" and player2 == "rock":
    print(f"{player1name} wins")
    plr1score += 1
elif player1 == "scissors" and player2 == "paper":
    print(f"{player1name} wins")
    plr1score += 1
else:
    print(f"{player2name} wins")
    plr2score += 1

print(f"Score: {player1name} {plr1score} - {player2name} {plr2score}")
