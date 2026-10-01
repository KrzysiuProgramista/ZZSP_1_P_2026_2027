side1= float(input("The length of the first side "))
side2= float(input("The length of the second side "))
side3= float(input("The length of the third side "))

if side1 > side2 + side3 or side2 > side1+side3 or side3 >side1+side2:
    print("This is NOT a triangle")

if side1 <side2+side3 or side2 < side1+side3 or side3 < side1+side2:
    print("this is a triangle.")

Obwod = side1+side2+side3

if side1 == side2 == side3:
    print("its the equality triangle")
elif side1==side2 or side1==side3 or side3 ==side2:
    print("its the isosceles triangle")
else:
    print("its scalene triangle")