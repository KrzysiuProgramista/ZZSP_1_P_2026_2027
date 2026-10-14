order_value = float(input("Enter order value: "))
if order_value < 0:
    print("invalid order value")
else:
    if order_value < 100:
        discount_percent = 0
    elif order_value < 300:
        discount_percent = 5
    elif order_value < 1000:
        discount_percent = 10
    else:
        discount_percent = 15

    discount_amount = order_value * (discount_percent / 100)
    final_price = order_value - discount_amount

    print(f"Discount percentage: {discount_percent:.2f}%")
    print(f"Discount amount: {discount_amount:.2f} PLN")
    print(f"Final price: {final_price:.2f} PLN")
