length1 = int(input('write first length'))
length2 = int(input('write seacond length'))
length3 = int(input('write third length'))
if length1 + length2 > length3 and length1 + length3 > length2 and length2 + length3 > length1 :
    print(' it is a triangle')
if length1 == length2 == length3 :
    print('equilateral')
elif length1 == length2 or length1 == length3 or length2 == length3 :
     print('isosceles')
else:
 print('scalene')

    
