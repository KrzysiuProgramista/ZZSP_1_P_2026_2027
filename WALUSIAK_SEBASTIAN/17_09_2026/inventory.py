inventory = [
    ["apple", 50],
    ["banana", 20],
    ["milk", 15],
    ["bread", 30]
]

amounts = [inventory[0][1], inventory[1][1], inventory[2][1], inventory[3][1]]
max_amount = max(amounts)
index = amounts.index(max_amount)

print("Product with the highest quantity:", inventory[index])

inventory.append(["cheese", 40])
inventory.sort()

print("Sorted inventory:")
print(inventory)
