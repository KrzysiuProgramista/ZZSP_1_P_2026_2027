value = float(input("give order value: "))

if value < 100:
    result = value
elif 100 <= value <= 299.99:
    print("5%")
    result = value - (value * 0.05)
elif 300 <= value <= 999.99:
    print("10%")
    result = value - (value * 0.10)
else:
    print("15%")
    result = value - (value * 0.15)

print(result)