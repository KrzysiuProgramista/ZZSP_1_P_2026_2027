sides = []

sides.append(int(input("First side: ")))
sides.append(int(input("Second side: ")))
sides.append(int(input("Third side: ")))

sort = (sorted(sides))

if sort[0] + sort[1] > sort[2]:
    print("is a triangle")
else:
    print("isn't a triangle")