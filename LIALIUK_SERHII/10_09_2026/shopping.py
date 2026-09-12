Name_Product = input("Print the name of the product you want: ")

Price = float(input("Print the price of the product: "))

Quanity = int(input("Print the quantity of the product you want: "))

Total = Price * Quanity 

print(f"{Quanity} x {Name_Product} = {Total:.2f} PLN")