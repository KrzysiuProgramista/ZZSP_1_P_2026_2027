orders = []
meal_types = ("sandwich", "salad", "soup", "hot meal", "other")

def addOrder(customer, meal):
    if meal in meal_types:
        orders.append({"customer": customer,
                       "meal": meal,
                       "served": False})
        print("added")
    else:
        print("meal is not in the list")

def show_orders(orders, show_served=False):
    if len(orders) == 0:
        print("nothing to show")
    else:
        for i in range(len(orders)):
            if show_served == False or orders[i]["served"] == True:
                print(i + 1, "-", orders[i]["customer"], " ", orders[i]["meal"], " served:", orders[i]["served"])

def markOrderAsServed(number):
    orders[number - 1]["served"] = True
    print("done")



while True:
    whatUserWants = int(input("What u want (0 - Add order, 1 - Show orders, 2 - Mark order served, 3 - display not done orders, 4 - exit application)"))
    if whatUserWants == 0:
        customerInput = input("Customer: ")
        mealInput = input("Meal: ")
        addOrder(customerInput, mealInput)
    elif whatUserWants == 1:
        show_orders(orders)
    elif whatUserWants == 2:
        number = int(input("Enter a order number: "))
        markOrderAsServed(number)
    elif whatUserWants == 3:
        show_orders(orders, only_unserved=True)
    elif whatUserWants == 4:
        exit()
