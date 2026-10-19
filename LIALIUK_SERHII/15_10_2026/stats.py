number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the fourth number: "))
number5 = int(input("Enter the fifth number: "))
numbers = [number1, number2, number3, number4, number5]
total = 0
for i in range(len(numbers)):
    total += numbers[i]
print("The sum is:",total)
average = total / len(numbers)
print("The average is:",average)
largest = numbers[0]
smallest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]
    if numbers[i] < smallest:
        smallest = numbers[i]
print("The largest number is:",largest)
print("The smallest number is:",smallest)
