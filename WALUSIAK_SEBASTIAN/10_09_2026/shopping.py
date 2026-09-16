name = input("Podaj nazwe produktu")
price = input("Podaj cene")
quantity = input("Podaj ilosc")

price = float(price)
quantity = int(quantity)

cost = price * quantity

print(f"{quantity} x {name} = {cost:.2f} PLN" )
