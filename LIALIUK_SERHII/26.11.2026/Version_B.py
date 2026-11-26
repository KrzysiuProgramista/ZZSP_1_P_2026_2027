checkouts = []
checkouts_returned = []
equipment_type =('laptop','camera','projuector','tablet','other')


# Checkout should be stored as this:
#{
# "borrower":"Jordan",
# "equipment":"camera",
# "returned": False
#}

def add_checkout(name,equipment_types):
    checkout = {
        "borrower": name,
        "equipment": equipment_types,
        "returned": False
    }
    checkouts.append(checkout)
    return name,equipment_types,checkout

def show_all_checkouts(checkouts):
    print(checkouts)
    return checkouts

def show_checkouts(checkouts,checkout):
    for checkouts in range(checkouts):
        if checkout["returned"] == False:
            print(checkout)
        else:
            continue
        return checkouts,checkout

def mark_returned(checkout,show_input):
    for checkouts in range(checkouts):
        if checkout["name"] == show_input:
                checkout["returned"] = True
            
                
    
    
    
        
        
        

    



def main():
    while True:
        print("-> Menu <-")
        print("\n1. Add a new checkout")
        print("2. Show the checkouts")
        print("3. Show the checkouts which is not returned")
        print("4. Change the status to the returned")
        print("0. Exit")

        main_input=input("\nPlease for continue print a number for to choose options: ")

        if main_input == "":
            print("Im sorry,The input can't be empty")
            continue
        elif main_input == "1":
            name = input("please give me the name of the borrower: ")
            while not name.strip():
                print("Name cannot be empty")
                name = input("please give me the name of the borrower: ")
                continue
            equipment_types = input("Give me the name of the equipment,The equipment types is: Laptop,Camera,Projector,Tablet,Other: ")
            while not equipment_types.strip():
                print("you can't save this record with no borrowed equipment")
                equipment_types = input("Give me the name of the equipment,The equipment types is: Laptop,Camera,Projector,Tablet,Other: ")
                continue
            if equipment_types.lower() not in equipment_type:
                print("You can't save this record with this equipment,please try again")
                equipment_types = input("Give me the name of the equipment,The equipment types is: Laptop,Camera,Projector,Tablet,Other: ")
                continue
            add_checkout(name,equipment_types)
            print("Checkout succesfully created.")
        elif main_input == "2":
            if checkouts == None:
                print("please,make a record first")
            show_all_checkouts(checkouts)
        elif main_input == "3":
            print("WIP,please try again later")
            continue
        elif main_input == "4":
            show_input = input("please print the name for finding a checkout")
            if show_input == checkouts["name"]:
                print(checkouts["name"])
                mark_returned()
        elif main_input == "0":
            print("Goodbye!!!!")
            break
        else:
            print("Invalid key,im sorry :(")
            continue
if __name__ == "__main__":
    main()