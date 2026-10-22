value = float(input("What's value you want in PLN(only numbers without PLN please): "))


if value < 0:
    print("Invalud order value")
elif value < 100:
    print("No discount")
    print(value)
elif value <300:
    print("5% discount")
    print(value * 0.05)
    print(value - (value * 0.05 ))
elif value <1000:
    print("10% discount")
    print(value * 0.1)
    print(value - (value * 0.1))
else:
    print("15% discount")
    print(value * 0.15)
    print(value - (value*0.15))