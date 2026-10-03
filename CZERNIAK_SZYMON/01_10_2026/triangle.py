side1 = int(input('Write down first side length:'))
side2 = int(input('Write down second side length:'))
side3 = int(input('Write down third side length:'))

if side1 >= side2 + side3 or side2 >= side1 + side3 or side3 >= side1 + side2:
    print('This can not be triangle')
else:
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        print('This can be the triangle.')
    
    if side1 == side2 != side3 or side1 == side3 != side2 or side2 == side3 != side1:
        print('This triangle is isosceles')
    if side1 == side2 == side3:
        print('This triangle is equilateral')
    if side1 != side2 != side3:
        print('This triangle is scalene')
    if side1 > side2 + side3 or side2 > side1 + side3 or side3 > side1 + side2:
        print('This can not be triangle')
