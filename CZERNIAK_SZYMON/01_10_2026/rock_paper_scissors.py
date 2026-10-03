Rock = 'Rock'
Paper = 'Paper'
Scissors = 'Scissors'

player1 = input(f'Player 1: {Rock}, {Paper} or {Scissors}:')
player2 = input(f'Player 2: {Rock}, {Paper} or {Scissors}:') 

if player1 == Rock and player2 == Scissors:
    print('Player 1 won')
elif player1 == Rock and player2 == Paper:
    print('Player 2 won')
elif player1 == Paper and player2 == Scissors:
    print('Player 2 won')
elif player1 == Paper and player2 == Rock:
    print('Player 1 won')
elif player1 == Scissors and player2 == Paper:
    print('Player 1 won')
elif player1 == Scissors and player2 == Rock:
    print('Player 2 won')
elif player1 == Rock and player2 == Rock:
    print('It is draw')
elif player1 == Paper and player2 == Paper:
    print('It is draw')
elif player1 == Scissors and player2 == Scissors:
    print('It is draw')
else:
    print('Invalid choice')
