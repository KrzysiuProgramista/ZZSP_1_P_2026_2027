player1 = input('choose a rock paper or scissors:')
player2 = input('choose a rock paper or scissors:')
if player1 not in ["rock", "paper", "scissors"] or player2 not in ["rock", "paper", "scissors"]:
    print('invalid choice')
elif player1 == player2 :
    print('draw')
elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "paper" and player2 == "rock") or \
     (player1 == "scissors" and player2 == "paper"):
    print('player 1 wins this round')
else:
    print('player 2 wins this round')
