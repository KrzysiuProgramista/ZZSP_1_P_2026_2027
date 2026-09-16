productName = input("Name of the product: ")
productPrice = float(input("Price of the product: "))
productAmount = int(input("Amount of products: "))

print(f"{productAmount} x {productName} =", productPrice * productAmount)