stats = []

for i in range(5):
    n = int(input("Enter a number: "))
    stats.append(n)

s = 0
for num in stats:
    s += num
print("The sum of the numbers you input is:", s)

a = 0
for num in stats:
    a = s / 5
print("The average of the numbers you input is:", a)

max = stats[0] #temporarily assign the max to the first element, the for loop will change it to the biggest in the list
for num in stats:
    if num > max:
        max = num
print("The biggest number you input is:", max)

min = stats[0] #temporarily assign the min to the first element, the for loop will change it to the smallest in the list
for num in stats:
    if num < min:
        min = num
print("The smallest number you input is:", min)
