nums = []

for i in range(5):
    num = float(input("enter a number: "))
    nums.append(num)

tot = 0

for num in nums:
    tot += num

aver = tot / len(nums)

large = nums[0]
small = nums[0]

for num in nums:
    if num > large:
        large = num

    if num < small:
        small = num

print("sum:", tot)
print("average:", aver)
print("largest:", large)
print("smallest:", small)