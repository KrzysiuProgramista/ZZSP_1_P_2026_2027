inventory = [['bread', 2], ['milk', 4], ['eggs', 30], ['ham', 3]]

print(inventory[2])

inventory.append(['cheese', 5])

inventory.sort(key=lambda x: x[0])
print(inventory)