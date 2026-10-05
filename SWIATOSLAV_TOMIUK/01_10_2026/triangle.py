a = float(input("side 1: "))
b = float(input("side 2: "))
c = float(input("side 3: "))

if a < b + c and b < a + c and c < a + b:
    print("triangle")
    if a == b and b == c:
        print("equilateral")
    elif a == b or b == c or a == c:
        print("isosceles")
    else:
        print("scalene")
else:
    print("not a triangle")