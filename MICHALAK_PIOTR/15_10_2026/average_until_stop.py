numbers = []

while True:
    Input = input("Input number or stop to stop: ")

    if Input == "stop":
        break

    try:
        numbers.append(int(Input))
    except ValueError:
        print("This ain't a number of the word stop. Try again.")


print("Numbers entered:", len(numbers))

if len(numbers) < 0:
    print("The average equals:", sum(numbers) / len(numbers))
else:
    print("No numbers, no average")
