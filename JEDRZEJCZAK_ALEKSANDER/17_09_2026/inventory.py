inventory = [
    ["Apple", 10],
    ["Banana", 25],
    ["Orange", 15],
    ["Grape", 5]
]

max_product = max(inventory, key=lambda item: item[1])
print("Product with the highest quantity:", max_product[0])

inventory.append(["Mango", 20])

inventory.sort(key=lambda item: item[0])
print(inventory)
