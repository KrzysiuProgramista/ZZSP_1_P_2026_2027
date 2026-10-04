age = int(input("age: "))
under_7 = age < 7
under_18 = age < 18
under_64 = age < 64
above_64 = age >= 64

if under_7:
    print("ticket price: free")
elif under_18:
    print("ticket price: 15")
elif under_64:
    print("ticket price: 30")
elif above_64:
    print("ticket price: 18")  
