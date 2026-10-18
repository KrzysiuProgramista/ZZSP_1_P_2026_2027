total = 0
count = 0

while True:
    value = input("enter a number or stop: ")

    if value == "stop":
        break

    number = float(value)
    total = total + number
    count = count + 1

print("numbers entered:", count)

if count > 0:
    average = total / count
    print("average:", average)
else:
    print("no numbers entered")
