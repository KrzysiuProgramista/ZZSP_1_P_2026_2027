product = input("Product name: ")
price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

total = price * quantity

print(quantity, "x", product, "=", round(total, 2), "PLN")
