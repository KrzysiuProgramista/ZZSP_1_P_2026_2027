a = int(input("Podaj pierwszy bok: "))
b = int(input("Podaj drugi bok: "))
c = int(input("Podaj trzeci bok: "))

if a + b > c and a + c > b and b + c > a:
    print("Można zbudować trójkąt")

    if a == b and b == c:
        print("Trójkąt równoboczny")
    elif a == b or a == c or b == c:
        print("Trójkąt równoramienny")
    else:
        print("Trójkąt różnoboczny")
else:
    print("Nie można zbudować trójkąta")
