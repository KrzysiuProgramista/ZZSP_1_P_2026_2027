p1 = input("player 1 (rock/paper/scissors): ").lower()
p2 = input("player 2 (rock/paper/scissors): ").lower()

if p1 != "rock" and p1 != "paper" and p1 != "scissors":
    print("player 1 made an invalid choice")
elif p2 != "rock" and p2 != "paper" and p2 != "scissors":
    print("player 2 made an invalid choice")
elif p1 == p2:
    print("draw")
elif p1 == "rock" and p2 == "scissors":
    print("player 1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("player 1 wins")
elif p1 == "paper" and p2 == "rock":
    print("player 1 wins")
else:
    print("player 2 wins")