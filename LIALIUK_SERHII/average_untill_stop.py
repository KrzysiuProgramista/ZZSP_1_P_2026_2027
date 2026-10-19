total = 0
count = 0
while True:
    user_input = input("Enter a number (or 'stop' to finish): ")
    if user_input == "stop":
        break
    number = float(user_input)
    total += number
    count += 1
print("Numbers entered:", count)
if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No numbers were found.")
