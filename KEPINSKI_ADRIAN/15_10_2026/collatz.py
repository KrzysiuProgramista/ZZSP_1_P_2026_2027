n = int(input("enter a positive int: "))

while n <= 0:
    n = int(input("enter a positive int: "))

steps = 0
print(n)

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    print(n)
    steps = steps + 1

print("steps:", steps)