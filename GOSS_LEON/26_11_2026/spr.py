checkouts = []
equipment_types = ("laptop", "camera", "projector", "tablet", "other")

def add_checkout(checkouts, equipment_types):
        borrower = input("who borrowed equipment: ")
        types = input("enter a type of equipment")
        if types not in equipment_types:
            types = "other"
        check = {
            "borrower": borrower,
            "equipment": types,
            "returned": False
        }
        checkouts.append(check)
        print("checkout added succsesfully")
def show_checkouts(checkouts, show_outstanding=False):
    for i in range(len(checkouts)):
        record = checkouts[i]
        if show_outstanding == False or record["returned"] == False:
            print(i + 1, record["borrower"], record["equipment"], record["returned"])
def marked_returned(checkouts):
        borrower = input("enter the borrowers name: ")
     
        for check in checkouts:
             if check["borrower"].lower() == borrower.lower():
                 check["borrower"] = True
                 print("checkout marked as returned!")
                 return
     
        print("checkout not found!")
     
     
while True:
         print(" reading list ")
         print("1. add checkout")
         print("2. show all checkouts")
         print("3. show returned checkouts")
         print("4. marked as returned")
         print("5. exit")
     
         choice = input("choose an option: ")
     
         if choice == "1":
             add_checkout(checkouts, equipment_types)
     
         elif choice == "2":
             show_checkouts(checkouts, equipment_types)
     
         elif choice == "3":
             show_checkouts(checkouts, True)
     
         elif choice == "4":
             marked_returned(checkouts)
     
         elif choice == "5":
             print("goodbye!")
             break
     
         else:
             print("invalid choice. try again.")
    
