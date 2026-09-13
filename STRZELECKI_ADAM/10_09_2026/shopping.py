product_name = input("Enter a product name: ")
unit_price = float(input("Enter a price (PLN) "))
quantity = int(input("Enter a quantity "))

total_cost = unit_price * quantity
print(quantity, "x", product_name, "=", total_cost, "PLN")
