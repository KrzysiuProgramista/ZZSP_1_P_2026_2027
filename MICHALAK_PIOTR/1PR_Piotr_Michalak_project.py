orders = []
meal_types = ("sandwich","salad","soup","hot meal","other")
program = None
run = True

def showCommands():
    print("1 - Add a new record")
    print("2 - Display all records")
    print("3 - Display records that still require action")
    print("4 - Update a selected record status to True")
    print("0 - Exit the application")

def add_order():
    name = input("Enter name: ")
    meal = input("Enter meal: ")
    if meal not in meal_types:
        meal = "other"
    orders.append({
        "customer": name,
        "meal": meal,
        "served": False
    })

def show_orders():
    print(orders)

def show_notFin_orders():
    for i in range(0,len(orders)):
        if orders[i]["served"] == False:
            print(orders[i])

def finishOrder():
    n = int(input("Input order number: "))
    orders [n-1]["served"] = True

while run:
    program = int(input("1 - Add a new record\n"
    "2 - Display all records\n"
    "3 - Display records that still require action\n"
    "4 - Update a selected record status to True\n"
    "0 - Exit the application\n"
    "Enter the number that corresponds to the program: "))

    if program == 1:
        add_order()
    elif program == 2:
        show_orders()
    elif program == 3:
        show_notFin_orders()
    elif program == 4:
        finishOrder()
    elif program == 0:
        run = False
    else:
        print("Pick one of the options.")