order = float(input("print the current value you want: "))

if order < 100:
    print("No discount")
    print("0 pln")
    print(order,"PLN")
elif order < 299.9:
    print("5% Discount")
    print(order * (1/20))
    print(round(order-(order*(1/20))),"PLN")
elif order < 999.99:
    print("10% discount")
    print(order * (1/10))
    print(round(order-(order*(1/10))),"PLN")
elif order >=1000:
    print("15% discount")
    (print(order * (1/7)))
    (print(round(order-(order*(1/7))),"PLN"))
