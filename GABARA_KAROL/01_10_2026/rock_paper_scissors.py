player1 = input("Gracz 1 (kamien/papier/nozyce): ")
player2 = input("Gracz 2 (kamien/papier/nozyce): ")

if player1 not in ["kamien", "papier", "nozyce"] or player2 not in ["kamien", "papier", "nozyce"]:
    print("Nieprawidlowy wybor")
elif player1 == player2:
    print("Remis")
elif (player1 == "kamien" and player2 == "nozyce") or \
     (player1 == "papier" and player2 == "kamien") or \
     (player1 == "nozyce" and player2 == "papier"):
    print("Wygrywa gracz 1")
else:
    print("Wygrywa gracz 2")
