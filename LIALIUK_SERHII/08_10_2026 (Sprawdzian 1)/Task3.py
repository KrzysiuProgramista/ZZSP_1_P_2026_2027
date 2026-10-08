list = [12312,132,1515,146143,13244,9999,6666,12341]
print(list)
print(max(list),min(list),sum(list)/len(list))
print(sorted(list,reverse=True))
print(list[0:3],list[5:8])

list.pop()
list.append("0")
print(list)