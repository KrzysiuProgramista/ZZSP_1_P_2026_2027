count = 0
total_sum = 0

while True:
    user_input = input("give me number or write 'stop' : ")
    
    if user_input.lower() == "stop":
        break
    
    try:
        number = float(user_input)
        total_sum += number
        count += 1
    except ValueError:
        print("incorect value, write number or 'stop'.")

if count == 0:
    print("No numbers detected.")
else:
    average = total_sum / count
    print(f"numbers: {count}")
    print(f"average: {average}")
