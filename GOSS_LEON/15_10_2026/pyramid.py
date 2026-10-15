height = int(input("pick a hight for pyramid "))
for j in range(height):
    space = height - j - 1
    stars = 2 * j + 1
    print(" " * space + "*" * stars)
