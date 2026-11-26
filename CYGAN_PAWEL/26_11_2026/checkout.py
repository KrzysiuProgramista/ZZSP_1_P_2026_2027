import sys
checkouts = [{"borrower": "Quandaledingle" ,"equipment":"laptop","returned": False},{"borrower": "Epstein" ,"equipment":"camera","returned": False}]
equipment = ("laptop","camera","projector","tablet","other")
print(
    "1 - Add checkout\n"
    "2 - Show checkouts\n"
    "3 - show returned\n"
    "4 - Mark as returned\n"
    "5 - Show equipment types\n"
    "0 - Exit the program\n"
)
def add_checkout():
    borrowers_name = input("Enter the borrowers name: ")
    equipment_name = input("Enter the equipment type: ").strip().lower()
    if equipment_name not in equipment:
        equipment_name = "other"
    checkouts.append({
        "borrower": borrowers_name,
        "equipment":equipment_name,
        "returned": False
    })
def show_checkout():
    for i in checkouts:
        print("Checkouts name: ",i["borrower"],"Equipments name: ",i["equipment"],"Returned: ", i["returned"])
def show_returned_checkouts():
    number = 0
    for i in checkouts:
        number += 1
        print(number, i["borrower"])
def mark_as_returned():
    num = 0
    for i in checkouts:
        num += 1
        print(num, i["borrower"])
    number_ask = int(input("Enter the checkouts number: "))
    if 1 <= number_ask <= len(checkouts):
        checkouts[number_ask - 1]
        i["returned"] = True
    else:
        print("spierbombiaj")
def show_equipment():   
    print(equipment)
user_pick = 100000
while user_pick != 0:
    user_pick = int(input("Enter your option pick: "))
    if user_pick == 1:
        add_checkout()
        print(
                "1 - Add checkout\n"
                "2 - Show checkouts\n"
                "3 - show returned\n"
                "4 - Mark as returned\n"
                "5 - Show equipment types\n"
                "0 - Exit the program\n"
            )
    elif user_pick == 2:
        show_checkout()
        print(
                "1 - Add checkout\n"
                "2 - Show checkouts\n"
                "3 - show returned\n"
                "4 - Mark as returned\n"
                "5 - Show equipment types\n"
                "0 - Exit the program\n"
            )
    elif user_pick == 3:
        show_returned_checkouts()
        print(
                "1 - Add checkout\n"
                "2 - Show checkouts\n"
                "3 - show returned\n"
                "4 - Mark as returned\n"
                "5 - Show equipment types\n"
                "0 - Exit the program\n"
            )
    elif user_pick == 4:
        mark_as_returned()
        print(
                "1 - Add checkout\n"
                "2 - Show checkouts\n"
                "3 - show returned\n"
                "4 - Mark as returned\n"
                "5 - Show equipment types\n"
                "0 - Exit the program\n"
            )
    elif user_pick == 5:
        show_equipment()

    elif user_pick == 0:
        sys.exit(0)
    else:
        print("spierbombiaj")
