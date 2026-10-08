zam =  float(input("what is the price in pln "))
rb = 0
if zam < 0:
    print("invalid price")
else:
    if zam < 100:
        rb = 0
    elif zam < 300:
        rb = 5
    elif zam < 1000:
        rb = 10
    else:
        rb = 15
print(f"{rb}%")
kr = zam * (rb / 100)
ck = zam - kr
print(f"{kr:.2f}pln")
print(f"{ck:.2f}pln")