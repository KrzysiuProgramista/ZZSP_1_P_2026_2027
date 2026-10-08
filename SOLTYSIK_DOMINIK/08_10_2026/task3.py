numbers = [12, 45, 3, 89, 23, 67, 1, 34]
largerst = max(numbers)
smallest = min(numbers)
avreage = sum(numbers)
print (f"najwieksza : {largerst}")
print (f"najmniejsza : {smallest}")
print (f"sredna : {avreage}")

sorted_desc = sorted(numbers, reverse=True)
print (f"posortowane malejąo : {sorted_desc}")

first_three = numbers[:3]
last_three = numbers[-3:]
print (f"pierw trzy : {first_three}")
print (f"ost trzy : {last_three}")

numbers.insert (0,99)
numbers.pop()
print(f"lista moduyfikacji: {numbers}")