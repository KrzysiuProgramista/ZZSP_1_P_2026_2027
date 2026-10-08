numbers = [12, 5, 27, 3, 18, 9, 42, 7]

print("largest:", max(numbers))
print("smallest:", min(numbers))
print("Avarage:",
      sum(numbers) / len(numbers))

numbers.sort(reverse=True)
print("sorted descending:", numbers)

print("first three:",
      numbers[:3])
print("last three:",
      numbers[-3:])

numbers.insert(0, 100)
numbers.pop()

print("final list:", numbers)