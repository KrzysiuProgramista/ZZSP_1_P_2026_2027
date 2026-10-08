value= float(input("Enter order value: "))
if value < 0:
    print("invalid order value")
else:
    if value < 100:
        discount = 0
    elif value < 300:
        discount = 5
    elif value < 1000:
        discount = 10
    else:
        discount = 15
        amount = value * discount / 100
        final = value - amount
        print(f"Discount precentage: {discount:.2f}%")
        print(f"Discount amount: {amount:.2f}")
        print(f"Final price: {final:.2f}")