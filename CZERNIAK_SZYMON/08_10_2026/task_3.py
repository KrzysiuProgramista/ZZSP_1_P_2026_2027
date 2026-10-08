numbers = [4, 2, 5, 1, 3, 6, 7, 8]

print(max(numbers)) 
print(min(numbers))
print(sum(numbers) // len(numbers)) #Max, min, avg

sorted_list = sorted(numbers, reverse=True)
print(sorted_list)

print(numbers[0:3])
print(numbers[-3:])

numbers.insert(0, 76)
numbers.pop()
print(numbers)
