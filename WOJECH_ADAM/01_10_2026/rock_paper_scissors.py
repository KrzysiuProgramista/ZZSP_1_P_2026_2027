p1 = input("player 1 - chose (rock/paper/scissors): ")
p2 = input("player 2 - chose (rock/paper/scissors): ")

vl = {"rock", "paper", "scissors"}

if p1 not in vl:
    print("invalid choice player 1: ", p1)
elif p2 not in vl:
    print("invalid choice player 2: ", p2)
elif p1 == p2:
    print("draw")
elif (p1 == "rock" and p2 == "scissors"):
     print("player 1 wins")
elif (p1 == "paper" and p2 == "rock"):
     print("player 1 wins")
elif (p1 == "scissors" and p2 == "paper"):
    print("player 1 wins")
else:
    print("player 2 wins")