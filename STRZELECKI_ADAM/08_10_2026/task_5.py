value = float(input("Enter the value of order: "))

if value < 0:
    print("Invalid order value")
    quit()
else:
    if value < 100:
        discount = 0
    elif value <= 299.99:
        discount = 5
    elif value <= 999.99:
        discount = 10
    else:
        discount = 15

discount_amount = round(value * (discount / 100), 2)
final_price = value - discount_amount

print(f"Discount procentage: {discount}%")
print(f"Discount amount: {discount_amount}")
print(f"Final price: {final_price}")
