imp = int(input("enter a positive integer: "))

while imp <= 0:
    inp = int(input("enter a positive integer: "))

stps = 0

print(imp)

while imp != 1:
    if imp % 2 == 0:
        imp = imp // 2
    else:
        imp = 3 * imp + 1

    print(imp)
    stps += 1