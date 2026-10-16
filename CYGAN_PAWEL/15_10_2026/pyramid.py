height = int(input("Enter the height of the pyramid: "))

for i in range(height):
    spaces = height - i - 1
    stars = 2 * i + 1

    print(" " * spaces + "*" * stars)
