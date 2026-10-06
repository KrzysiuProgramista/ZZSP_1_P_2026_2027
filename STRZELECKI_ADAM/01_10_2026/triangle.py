a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and a == c and b == c:
        print("The triangle is equilateral.")
    elif a == b or a == c or b == c:
        print("The triangle is isosceles.")
    elif a != b and a != c and b != c:
        print("The triangle is scalene.")
else:
    print("Those lenghts cannot form a triangle.")
