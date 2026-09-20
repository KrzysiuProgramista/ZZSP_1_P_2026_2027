nested_list = [
    ['apple', 4],
    ['bread', 2],
    ['pear', 3],
    ['orange', 5]
]

numbers = [nested_list[0][1], nested_list[1][1], nested_list[2][1], nested_list[3][1]]

max_number = max(numbers)

for product in nested_list:
    if product[1] == max_number:
        print(product[0])
