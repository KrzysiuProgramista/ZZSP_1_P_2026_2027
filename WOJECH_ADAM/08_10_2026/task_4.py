inp1 = float(input("give the first num: "))
inp2 = float(input("give the second num: "))
op = input("(+,-,*,/): ")
if op == '+':
    print(inp1 + inp2)
elif op == '-':
    print(inp1 - inp2)
elif op == '*':
    print(inp1 * inp2)
elif op == '/':
    if inp2 == 0:
        print("cant divide by 0")
    else:
        print(inp1 / inp2)