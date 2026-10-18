h = int(input("Enter the height of the pyramid: "))

for i in range(1, h + 1):
    for j in range(h - i):
        print(" ", end="")

    for k in range(1, i * 2):
        print("*", end="")
    print()
