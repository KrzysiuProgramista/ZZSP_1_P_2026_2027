orders = ['Not finished:' ]
finished_orders = ['Finished:' ]
meal_types = ("sandwich", "salad", "soup", "hot meal", "other")
drink_types = ("cola", "pepsi", "sprite", "water", "tea")

running = True

def add_meal(orders, meal_types, drink_types):
    """This function adds meal to the list of orders"""
    print(meal_types)
    new_meal = input("Add the meal: ")
    if new_meal in orders:
        print("Meal is already in list")
        return
    orders.append(new_meal)
    print("Order added succesfully")
    question = input("Do you want anything to drink")
    if question == "yes":
        print(drink_types)
        drink = input("What drink would you like?: ")
        if drink not in drink_types:
            print("We do not have that type of drink")
        orders.append(drink)
        print("Drink succesfully added")
    elif question == "no":
        pass

def show_orders(orders):
    """This function shows list of order finished and not finished"""
    print(orders)
    print(finished_orders)

def mark_finished(orders, finished_orders):
    print(orders)
    finished = input("Enter the order you finished: ")
    for order in orders:
        if finished in finished_orders:
            print("Order is already finished")
    orders.remove(finished)
    finished_orders.append(finished)
    print("Order marked as finished")


while running:
    print(""" 
    1. Add order
    2. Show orders
    3. Showed orders to do
    4. Mark as finished
    0. Exit """)
    choice = int(input("Choose what to do: "))
    if choice == 1:
        add_meal(orders, meal_types, drink_types)
    elif choice == 2:
        show_orders(orders)
    elif choice == 3:
        print(orders)
    elif choice == 4:
        mark_finished(orders, finished_orders)
    elif choice == 0:
        running = False
    else:
        print("Invalid choice")



