def main():
    try:
        user_age = int(input("Age: "))
    except ValueError:
        return print("Invalid input")

    tariffs = [
        (6, "Free"),
        (18, "15 PLN"),
        (64, "30 PLN"),
        (float('inf'), "18 PLN")
    ]

    for limit, price in tariffs:
        if user_age <= limit:
            print(f"Ticket price: {price}")
            break

main()
