n = int(input("Enter a positive integer: "))

if n < 1:
    print("Please enter a positive integer.")

steps = 0
while n != 1:
    if n % 2 == 0:
        n /= 2
        print(n)
        steps += 1
    else:
        n = n * 3 + 1
        print(n)
        steps += 1
print("Total steps:", steps)
