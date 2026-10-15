number1 = int(input('pick a number'))
number2 = int(input('pick a number'))
number3 = int(input('pick a number'))
number4 = int(input('pick a number'))
number5 = int(input('pick a number'))
list = [number1, number2, number3, number4, number5]
sum = number1 + number2 + number3 + number4 + number5
average = sum / 5
largest = number1
smallest = number1
for num in list:
    if num > largest:
        largest = num
if num < smallest:
    smallest = num
    print(sum)
    print(average)
    print(largest)
    print(smallest)
