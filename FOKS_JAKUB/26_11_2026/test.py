orders = []
meal_types = ("sandwich", "salad", "soup", "hot meal", "other")

def add_order(orders, meal_types):
    """Add a new customer order to the queue"""
    name = input("Enter customer name: ")

    print("Available meal types:", meal_types)
    meal_type = input("Enter the meal type: ")

    if meal_type not in meal_types:
        print("Invalid meal type. Using other.")
        meal_type = "other"

    order = {
        "customer": name,
        "meal": meal_type,
        "served": False
    }

    orders.append(order)
    print("Order added!")


def show_orders(orders, show_served=False):
    """Display all orders or only orders that are still pending."""
    if len(orders) == 0:
        print("The order list is empty.")
    else:
        for i in range(len(orders)):
            if show_served == False or orders[i]["served"] == True:
                print(i + 1, "-", orders[i]["customer"], "|", orders[i]["meal"], "| served:", orders[i]["served"])


def served_orders(orders):
    """Mark a selected order as served."""
    if len(orders) == 0:
        print("There are no orders.")
    else:
        show_orders(orders)

        try:
            number = int(input("Enter a order number: "))

            if number >= 1 and number <= len(orders):
                orders[number - 1]["served"] = True
                print("Order marked as served!")
            else:
                print("Invalid order number.")

        except ValueError:
            print("Please enter a number")

      running = True
while running:
    print("1. Add a new order")
    print("2. Display all orders")
    print("3. Display served orders only")
    print("4. Mark a order as served")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_order(orders, meal_types)

    elif choice == "2":
        show_orders(orders)

    elif choice == "3":
        show_orders(orders, True)

    elif choice == "4":
        served_orders(orders)

    elif choice == "0":
        running = False
        print("Goodbye!")

    else:
        print("Invalid option")
