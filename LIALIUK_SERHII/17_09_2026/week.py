week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

print(week[0:5])
print(week [5:7])

print(week[::-1])

#The difference of del,remove() and pop()

#The difference of "remove()" is what it removes the first matched(what basicly the character/value you need) value from the list,and removing it from.

Example_Remove = [1,2,2,3,4,5,6,7,8]

Example_Remove.remove(2)

print(Example_Remove)

#The difference of "pop()",what its can remove and return an element from the list(if there's case of being NO index(element) it will remove the last element).

Ex_Pop = [11,22,23,22,24,25,30]

Ex_Pop.pop(0)

print(Ex_Pop)

Ex_Pop.pop()

print(Ex_Pop)

#The difference of "del" is what it can delete items from a list by index or the entire list,it can aslo delete the whole slice in the list.

Ex_del = [0,1,2,3,4,5,5]

del Ex_del[5]

print(Ex_del)

del Ex_del[1:5]

print(Ex_del)