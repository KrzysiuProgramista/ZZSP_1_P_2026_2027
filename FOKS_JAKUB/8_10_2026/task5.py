Value = int(input("Enter your order value: "))

if Value < 0:
    print("Invalid order.")

else:
    if Value < 100:
        discount = 0
    elif Value < 300:
        discount = 5
    elif Value < 1000:
        discount = 10
    elif Value >= 1000:
        discount = 15

discount_amount = Value * discount / 100
price = Value - discount_amount

print(f"For {Value}PLN order, there is {discount}% discount. Final price is: {price}")
