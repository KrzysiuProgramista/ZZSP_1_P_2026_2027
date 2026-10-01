a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

if (a + b > c) & (b + c > a) & (c + a > b):
    print("These lenghts can make a triangle!")
    if (a == b) & (b == c) & (c == a):
        print("This triangle is equilateral!")
    elif ((a==b) or (a==c)):
        print("This triangle is isosceles!")
    elif ((a != b) & (b != c) & (c != a)):
        print("This triangle is scalene!")
else:
    print("These lenghts can't make a triangle!")
