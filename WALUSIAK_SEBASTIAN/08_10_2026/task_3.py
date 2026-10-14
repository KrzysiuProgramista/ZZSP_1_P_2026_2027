numbers = [12, 45, 7, 89, 23, 56, 3, 34]

largest = max(numbers)
smallest = min(numbers)
average = sum(numbers) / len(numbers)

print(f"Largest: {largest}, Smallest: {smallest}, Average: {average:.2f}")
sorted_desc = sorted(numbers, reverse=True)
print("Sorted descending:", sorted_desc)

first_three = numbers[:3]
last_three = numbers[-3:]

print("First three:", first_three)
print("Last three:", last_three)

numbers.insert(0, 99)
numbers.pop()

print("Updated list:", numbers)
