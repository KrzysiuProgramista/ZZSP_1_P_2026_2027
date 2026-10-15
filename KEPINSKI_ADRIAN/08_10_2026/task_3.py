numbers = [5,7,1,4,8,9,2,44]
print("largest : ", max(numbers))
print("smallest :", min(numbers))
print(sorted(numbers, reverse=True))
print("first three : ", numbers[0:3])
print("last three : ", numbers[-3:])
numbers.insert(0,67)
numbers.pop(-1)
print("after modifications :", numbers)

print(numbers[-1])