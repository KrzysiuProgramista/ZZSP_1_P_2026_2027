a = float(input("Tell me first length"))
b = float(input("Tell me second length"))
c = float(input("Tell me third length"))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle is possible")
    if a == b and b == c:
        print("equilateral.")
    elif a == b or a == c or b == c:
        print("isosceles")
    else:
        print("scalene")
else:
    print("Triangle is not possible")
