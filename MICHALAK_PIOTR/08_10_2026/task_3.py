lis = [1,3,5,9,6,28,257,9275]
print(max(lis),min(lis), sum(lis)/len(lis))
print(sorted(lis,reverse=True))
print(lis[0:3],lis[5:8])
lis.pop(-1)
lis.insert(0, 2)
print(lis)