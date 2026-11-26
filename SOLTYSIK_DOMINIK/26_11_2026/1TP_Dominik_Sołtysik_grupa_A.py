def add_order(orders, meal_types):
    """Add a new customer order to the queue."""
    customer = input("Enter customer name: ").strip()

    if customer == "":
        customer = "Unknown"

    print("Available meal types:")
    for meal in meal_types:
        print("-", meal)

    meal = input("Enter meal type: ").strip().lower()

    if meal not in meal_types:
        print("Invalid meal type. Setting meal to 'other'.")
        meal = "other"

    order = {
        "customer": customer,
        "meal": meal,
        "served": False
    }

    orders.append(order)
    print("Order added successfully!")


def show_orders(orders, show_pending=False):
    """Display all orders or only orders waitingz."""
    if len(orders) == 0:
        print("no orders.")
    else:
        found = False

        for number, order in enumerate(orders, start=1):
            if not show_pending or not order["served"]:
                status = "Served" if order["served"] else "Waiting"

                print(
                    f"Order {number}: "
                    f"Customer: {order['customer']} | "
                    f"Meal: {order['meal']} | "
                    f"Status: {status}"
                )
                found = True

        if not found:
            print("There are no pending orders.")


def mark_order_served(orders):
    """Mark a selected order as served."""
    if len(orders) == 0:
        print("There are no orders to update.")
    else:
        show_orders(orders)

        try:
            number = int(input("Enter order number to mark as served: "))

            if 1 <= number <= len(orders):
                order = orders[number - 1]

                if order["served"]:
                    print("This order has already been served.")
                else:
                    order["served"] = True
                    print("Order marked as served!")
            else:
                print("Invalid order number.")

        except ValueError:
            print("Please enter a valid whole number.")


def main():
    """Run the canteen order queue application."""
    orders = []
    meal_types = (
        "sandwich",
        "salad",
        "soup",
        "hot meal",
        "other"
    )

    choice = ""

    while choice != "0":
        print("\n=== CANTEEN ORDER QUEUE ===")
        print("1. Add a new order")
        print("2. Display all orders")
        print("3. Display pending orders")
        print("4. Mark an order as served")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_order(orders, meal_types)
        elif choice == "2":
            show_orders(orders)
        elif choice == "3":
            show_orders(orders, show_pending=True)
        elif choice == "4":
            mark_order_served(orders)
        elif choice == "0":
            print("Exiting the application. Goodbye!")
        else:
            print("Invalid menu choice. Please try again.")


if __name__ == "__main__":
    main()