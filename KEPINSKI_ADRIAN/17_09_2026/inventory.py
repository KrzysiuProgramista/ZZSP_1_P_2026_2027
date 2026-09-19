inventory = [
    ["banana", 10],
    ["mango", 25],
    ["watermelon", 15],
    ["green apple", 8]
]

quantities = [
    inventory[0][1],
    inventory[1][1],
    inventory[2][1],
    inventory[3][1]
]

highest = max(quantities)

print(inventory[quantities.index(highest)])

inventory.append(["grapes", 12])

inventory.sort()

print(inventory)
