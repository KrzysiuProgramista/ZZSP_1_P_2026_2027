order_value = float(input("Enter your order value: "))
discount = 0
if order_value < 100:
    discount = 0
    print("0% off")
elif 100 <= order_value < 300:
    discount = 0.05
    print("5% off")
elif 300 <= order_value < 1000:
    discount = 0.10
    print("10% off")
else:
    discount = 0.15
    print("15% off")

final_price = order_value * (1 - discount)

print("final price:", round(final_price, 2))
