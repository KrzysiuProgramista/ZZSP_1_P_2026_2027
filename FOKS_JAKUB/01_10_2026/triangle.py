Side1 = int(input("Pick first side lenght: "))
Side2 = int(input("Pick second side lenght: "))
Side3 = int(input("Pick third side lenght: "))

if Side1 + Side2 > Side3 or Side2 + Side3 > Side1 or Side1 + Side3 > Side2:
    print("They can form a triangle")
    if Side1 == Side2 and Side2 == Side3:
        print("Equilteral")
    elif Side1 == Side2 or Side1 == Side3 or Side2 == Side3:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("These sides cannot form a triangle")
