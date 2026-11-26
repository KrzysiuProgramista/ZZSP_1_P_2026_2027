def add_checkout(checkouts, equipment_types): 
    """Add a new equipment checkout record""" 
    borrower = input("Enter borrower name: ")

    print("Allowed equipment types:", ", ".join(equipment_types))
    equipment = input("Enter equipment type: ")

    if equipment not in equipment_types:
        print(f"Invalid equipment type '{equipment}'. Storing as 'other'.")
        equipment = "other"

    record = {
        "borrower": borrower,
        "equipment": equipment,
        "returned": False
    }
    checkouts.append(record)
    print("Checkout record added successfully.")

def show_checkouts(checkouts, show_out=False): 
    """Display all checkouts or only equipment not yet returned""" 
    if not checkouts:
        print("Not anything in checkouts.")
        return

    found = False
    for index, record in enumerate(checkouts, start=1):
        if show_out and record["returned"]:
            continue
        status = "Returned" if record["returned"] else "Not returned"
        print(f"{index}. Borrower: {record['borrower']} | Equipment: {record['equipment']} | Status: {status}")
        found = True

    if not found and show_out:
        print("All equipment has been returned (no outstanding checkouts)")

def mark_returned(checkouts): 
    """Mark a selected checkout as returned""" 
    if not checkouts: 
        print("No checkout records available to update")
        return

    show_checkouts(checkouts)
    choice = input("Enter the checkout number to mark as returned: ")

    if choice.isdigit():
        checkout_num = int(choice)
        if 1 <= checkout_num <= len(checkouts):
            checkouts[checkout_num - 1]["returned"] = True
            print(f"Checkout #{checkout_num} marked as returned")
        else:
            print("Error: Checkout number is out of range")
    else:
        print("Error: Please enter a valid number")

def main(): 
    """Run the main menu loop for the Equipment Checkout Manager""" 
    checkouts = []
    equipment_types = ["laptop","camera", "projector", "tablet", "other"]

    print("Equipment Checkout Manager initialized. Type 'help' for options")

    while True:
        inp1 = input("\ncomma: ").strip().lower()

        if inp1 == "add":
            add_checkout(checkouts, equipment_types)
        elif inp1 == "showd":
            show_checkouts(checkouts, show_out=True)
        elif inp1 == "shownd":
            show_checkouts(checkouts, show_out=False)
        elif inp1 == "returned":
            mark_returned(checkouts)
        elif inp1 == "exit":
            print("Exiting Equipment Checkout Manager")
            break
        elif inp1 == "help":
            print("\n--- Help Menu ---")
            print("add         - Add a new record")
            print("showd    - Display all records")
            print("shownd - Display records that still require action")
            print("returned    - Update a selected record status to True")
            print("exit        - Exit the application")
        else:
            print("not a comma use 'help'")

if __name__ == "__main__":
    main()