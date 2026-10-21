result = 0
num = []

for i in range(5):
    num.append(int(input("Insert number: ")))

#Sum of the numbers
print("Sum:")
for i in range(len(num)):
    result += num[i]
print(result)
result = 0
#Largest number
print("Max:")
for i in range(len(num)):
    if result < num[i]:
        result = num[i]
print(result)
#Smallest number
print("Min:")
for i in range(len(num)):
    if result > num[i]:
        result = num[i]
print(result)