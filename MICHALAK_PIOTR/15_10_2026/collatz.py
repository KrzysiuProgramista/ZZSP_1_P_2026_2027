steps = 0
n = int(input("Input positive 'n'"))
if n <= 0:
    print("I said positive")
    exit()

while n != 1:
    steps += 1
    if n % 2 == 0:
        n /= 2
    else:
        n = (3*n + 1)

print(f"It took {steps} steps to get to 1")
