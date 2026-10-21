total = 0
count = 0
req = "enter a number or stop: "

text = input(req)

while text != "stop":
    number = float(text)
    total = total + number
    count = count + 1

    text = input(req)

print("numbers entered:", count)

if count > 0:
    print("average:", total / count)
else:
    print("no numbers were enteredd")