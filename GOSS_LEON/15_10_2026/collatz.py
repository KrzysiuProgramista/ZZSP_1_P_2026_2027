n = int(input("write a positive integer: "))

steps = 0
while n != 1:
    print(n)
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1

    steps = steps + 1
print(1)
print("steps ", steps)
