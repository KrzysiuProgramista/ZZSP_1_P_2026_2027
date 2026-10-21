numbers = []

for i in range(5):
    number = float(input("enter a number: "))
    numbers.append(number)

total = 0
largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    total = total + number

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("sum:", total)
print("average:", total / 5)
print("largest:", largest)
print("smallest:", smallest)