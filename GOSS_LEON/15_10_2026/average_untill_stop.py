total = 0
count = 0
while True:
    user = input("write number here (or 'stop' to end)")
    if user == "stop":
        break
    num = float(user)
    total = total + num
    count = count + 1
if count == 0:
    print("no numbers here")
else:
    average = total / count
    print(count)
    print(average)
