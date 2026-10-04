a = float(input("side a: "))
b = float(input("side b: "))
c = float(input("side c: "))

ok = a + b > c and a + c > b and b + c > a

if ok:
    print("triangle ok")
else:
    print("triangle not ok")
