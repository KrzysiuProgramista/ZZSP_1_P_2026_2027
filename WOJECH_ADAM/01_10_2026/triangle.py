a = float(input("side a: "))
b = float(input("side b: "))
c = float(input("side c: "))

if a + b > c and a + c > b and b + c > a:
    print("can make a triangle")
    if a == b == c:
        print("equilateral triangle")
    elif a == b or a == c or b == c:
        print("isosceles triangle")
    else:
        print("scalene triangle")
else:
    print("can't make a triangle")