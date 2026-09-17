inventory = [["grape", 45], ["Apple", 120], ["orange", 30], ["pear", 60]]
print(max(inventory, key=lambda x: x[1])[0])
inventory.append(["meat", 25])
inventory.sort(key=lambda x: x[0])
print("sorted:", inventory)
