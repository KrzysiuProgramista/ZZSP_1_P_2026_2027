total = 0
count = 0

while True:
    numbers = input('Enter a number or "stop": ')

    if numbers == "stop":
        break

    number = int(numbers)
    total += number
    count += 1

if count > 0:
    average = total / count
    print('Numbers:', count)
    print('Average:', average)
else:
    print('No numbers were entered')
