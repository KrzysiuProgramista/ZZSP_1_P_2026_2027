inventory = [
    ["Apple", 10],
    ["Banana", 25],
    ["Orange", 15],
    ["Milk", 8]
]

highest = max(inventory, key=lambda item: item[1])

print("Product with highest quantity:", highest[0])

inventory.append(["Bread", 12])

inventory.sort(key=lambda item: item[0])

print("Sorted inventory:")
print(inventory)