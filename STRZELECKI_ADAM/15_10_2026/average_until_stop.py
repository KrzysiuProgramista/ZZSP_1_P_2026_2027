print("Enter numbers one by one. Type 'stop' when you are finished.")

counter = 0
total = 0.0
running = True

while running:
    user_input = input("Enter a number (or 'stop'): ").strip()

    if user_input == 'stop':
        running = False
    else:
        try:
            number = float(user_input)
            total += number
            counter += 1
        except ValueError:
            print("Invalid number. Please enter a valid number or type 'stop' to finish.")

if counter == 0:
    print("No numbers entered. Exiting.")
else:
    average = total / counter
    print("Total number of numbers entered:", counter)
    print("The average is", average)
