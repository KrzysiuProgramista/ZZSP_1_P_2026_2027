age = int(input("age: "))
if age < 7:
    print("ticket is free")
elif 7 <= age <= 18:
    print("ticket is 15PLN")
elif 19 <= age <= 64:
    print("ticket is 30PLN")
else:  # 65+
    print("ticket is 18PLN")