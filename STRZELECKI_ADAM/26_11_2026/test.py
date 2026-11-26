checkouts = []
equipment_types = ("laptop", "camera", "projector", "tablet", "other")

def add_checkout(checkouts, equipement_types):
    """Add a new equipement checkout record."""
    name = input("Who borrowed an equipment: ")
    equipment = input("Equipment type:")
    if equipment not in equipment_types:
        equipment = "other"
    checkouts.append({"borrower": name, "equipment": equipment, "returned": False})

def show_checkouts(checkouts, show_outstanding=False):
    """Display all checkouts or only equipment not yet returned."""
    for i in range(len(checkouts)):
        record = checkouts[i]
        if show_outstanding == False or record["returned"] == False:
            print(i + 1, record["borrower"], record["equipment"], record["returned"])

def mark_returned(checkouts):
    """Mark a selected checkout as returned"""
    number = input("Checkout number: ")
    if number.isdigit() and 1 <= int(number) <= len(checkouts):
        checkouts[int(number) - 1]["returned"] = True
    else:
        print("Wrong number.")

running = True
while running:
    print("\n1 Add | 2 Show all | 3 Show no returned | 4 Mark returned | 0 Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_checkout(checkouts, equipment_types)
    elif choice == "2":
        show_checkouts(checkouts)
    elif choice == "3":
        show_checkouts(checkouts, True)
    elif choice == "4":
        mark_returned(checkouts)
    elif choice == "0":
        running = False
        exit
    else:
        print("Unknown choice.")
