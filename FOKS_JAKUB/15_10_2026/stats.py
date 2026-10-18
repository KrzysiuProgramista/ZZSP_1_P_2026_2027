numbers = []

for i in range(5):
    number = int(input("enter a number: "))
    numbers.append(number)

total = 0

for number in numbers:
    total = total + number

average = total / 5

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("sum:", total)
print("average:", average)
print("largest:", largest)
print("smallest:", smallest)
