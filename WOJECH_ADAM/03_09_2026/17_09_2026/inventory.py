inventory = [
    ["Jabłko", 20],
    ["Banan", 35],
    ["Pomarańcz", 15],
    ["Mleko", 40]
]
najwyższa = max(inventory, key=lambda item: item[1])
print("najwyższa quantity:", najwyższa[0], "-", najwyższa[1])
inventory.append(["Bread", 25])
inventory.sort(key=lambda item: item[0])
print("Sorted inventory:")
print(inventory)