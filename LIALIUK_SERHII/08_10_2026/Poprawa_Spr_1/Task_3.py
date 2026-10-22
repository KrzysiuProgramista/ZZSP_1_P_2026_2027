num = [2323,12312,15125124,1241231,51251,12312312,6523,676767]

total = sum(num) / len(num)

print(max(num),total,min(num))
print(sorted(num,reverse=True))
print(num[0:3],num[5:8])

num[0] = 0

print(num)