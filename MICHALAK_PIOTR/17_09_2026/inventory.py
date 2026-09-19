products = [
        ["bread", 4],
        ["cheese", 6],
        ["ham", 3],
        ["margarine", 5]
]
print(max(products, key=lambda x: x[1]))
products.append(
    ["sugar", 12]
)

print(sorted(products))