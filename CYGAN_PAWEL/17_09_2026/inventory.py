inventory = [["Bread", 3],["Milk", 2],["Nutella", 1],["Eggs", 12]]
inventory.sort(key=lambda row: row[1], reverse=True)
print(inventory[0])
inventory.append(["Chocolate", 3])
inventory.sort(key=lambda row: row[0].lower())
print(inventory)
