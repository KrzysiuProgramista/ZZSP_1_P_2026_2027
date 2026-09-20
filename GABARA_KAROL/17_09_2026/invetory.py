products = [
    ["banana", 35],
    ["milk", 60],
    ["bread", 15],
    ["cheese", 40]
]

print(max(products, key=lambda item: item[1])[0])

products.append(["water", 80])

products.sort(key=lambda item: item[0])

print("Sorted:", products)
