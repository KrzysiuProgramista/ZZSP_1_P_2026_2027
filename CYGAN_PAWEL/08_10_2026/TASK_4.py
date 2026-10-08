number_1 = float(input("Enter a number: "))
number_2 = float(input("Enter a second number: "))
operator = input("Enter a operator(+,=,*,/): ")
if operator == "+":
    print(number_1 + number_2)
elif operator == "-":
    print(number_1 - number_2)
elif operator == "*":
    print(number_1 * number_2)
elif operator == "/":
    if number_2 != 0:
        print(number_1 / number_2)
    else:
        print("Cannot divide by zero.")
else:
    print("Unknown operator.")
