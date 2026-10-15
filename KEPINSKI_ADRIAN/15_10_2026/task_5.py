value = float(input("Order value : "))

if value < 100:
    discount = 0.0
elif value < 300:
    discount = 0.05
elif value < 1000:
    discount = 0.10
else:
    discount = 0.15

amount = value * discount
final = value - amount

print(f"discount: {discount * 100:.0f}%")
print(f"discount amount: {amount:.2f}")
print(f"final value: {final:.2f}")