nums = [8,2,60,3,4,10,1,11]

print(min(nums), max(nums), sum(nums) / len(nums))
numss = sorted(nums)
print(numss[::-1])
print(nums[0:3])
print(nums[-3:])
nums.insert(0, 7)
nums.remove(11)
print(nums)
