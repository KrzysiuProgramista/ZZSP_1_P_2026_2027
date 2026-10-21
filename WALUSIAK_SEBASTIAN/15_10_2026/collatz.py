n = int(input("give me a positive integer: "))
steps = 0

print(n)

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    
    print(n)
    steps += 1

print(f"steps: {steps}")
