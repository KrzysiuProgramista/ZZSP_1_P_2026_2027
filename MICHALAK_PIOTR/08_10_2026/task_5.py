value = int(input("Enter order value: "))

if value < 100:
    print("0%")
    print("0 pln")
    print(value,"pln")
elif value >= 100 and value <= 299.99:
    print("5%")
    print(value * (1/20),"pln")
    print(value - (value * (1/20)),"pln")
elif value >= 300 and value<= 999.99:
    print("10%")
    print(value * (2/20),"pln")
    print(value - (value * (2/20)),"pln")
else:
    print("15%")
    print(value * (3/20),"pln")
    print(value - (value * (3/20)),"pln")