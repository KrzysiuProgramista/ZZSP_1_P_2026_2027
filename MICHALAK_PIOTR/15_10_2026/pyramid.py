def pyramid():
    height = int(input("Input heaight of pyramid: "))

    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

pyramid()