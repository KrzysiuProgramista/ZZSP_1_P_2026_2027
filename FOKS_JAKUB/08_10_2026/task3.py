numbers = [22, 23, 75, 17, 19, 62]

print(f"Largest:", max(numbers))
print(f"Smallest:", min(numbers))
print(f"Average:", sum(numbers) / len(numbers))

print("First three:", numbers[:3])
print("Last three:", numbers[-3:])

numbers.insert(0, 100)
numbers.pop()
print("Result:", numbers)
