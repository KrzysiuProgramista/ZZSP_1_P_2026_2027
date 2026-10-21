numbers = []

for i in range (5):
    number = float(input("podaj numer"))
    numbers.append(number)

total_sum = 0
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    total_sum += number
    if num > largest:
        largest = number
    if num < smallest:
        smallest = number

average = total_sum / len(numbers)

print(f"suma: {total_sum}")
print(f"srednia: {average}")
print(f"najwiekszaa: {largest}")
print(f"najmniejsza: {smallest}")
