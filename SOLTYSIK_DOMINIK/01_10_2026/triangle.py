a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if a < b + c and b < a + c and c < a + b:
    print("These sides can form a triangle.")

    if a == b == c:
        print("The triangle is equilateral.")
    elif a == b or a == c or b == c:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("These sides cannot form a triangle.")