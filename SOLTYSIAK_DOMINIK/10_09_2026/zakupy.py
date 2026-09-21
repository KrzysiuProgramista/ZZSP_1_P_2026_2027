product = input("Product name: ")
price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

total = price * quantity

print(f"{quantity} x {product} = {total:.2f} PLN")