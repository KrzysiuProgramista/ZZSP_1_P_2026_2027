Choice1 = input("Pick rock, paper or scissors: ")
Choice2 = input("Pick rock, paper or scissors: ")

if Choice1 == "rock" and Choice2 == "paper":
    print("Paper won.")
elif Choice1 == "rock" and Choice2 == "scissors":
    print("Rock won.")
elif Choice1 == "rock" and Choice2 == "rock":
    print("Draw.")

elif Choice1 == "paper" and Choice2 == "paper":
    print("Draw.")
elif Choice1 == "paper" and Choice2 == "scissors":
    print("Scissors won.")
elif Choice1 == "paper" and Choice2 == "rock":
    print("Paper won.")

elif Choice1 == "scissors" and Choice2 == "paper":
    print("Scissors won.")
elif Choice1 == "scissors" and Choice2 == "scissors":
    print("Draw.")
elif Choice1 == "scissors" and Choice2 == "rock":
    print("Rock won.")

else:
    print("Invalid choice.")
