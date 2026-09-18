inventory = [
    ["bananas", 10],
    ["apples", 5],
    ["cobblestone", 32],
    ["bread", 6]]

print(max(inventory, key=lambda item: item[1]))
inventory.append(["eggs", 60])
inventory.sort(key=lambda item: item[0])
print(inventory)