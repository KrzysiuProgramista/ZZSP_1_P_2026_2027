order_value = float(input("podaj wartosc zamowienia: "))
if order_value < 0:
    print("invalid price")
else:
    if order_value < 100:
        discount_pct = 0
    elif order_value < 300:
        discount_pct = 5
    elif order_value < 1000:
       discount_pct = 10
    else:
        discount_pct = 15
discount_ammound = order_value * (discount_pct / 100)
final_price = order_value - discount_ammound
print(f"discount preceage: {discount_pct:.2f}%")
print(f"discount ammount: {discount_ammound:.2f}")
print(f"final  price: {final_price:.2f}")
