ag = int(input("what is your age?: "))

if ag < 7:
    pr = 0
elif ag <= 18:
    pr = 15
elif ag <= 64:
    pr = 30
else:
    pr = 18
if pr == 0:
    print("free ticket")
else:
    print("ticket price: ", pr,"PLN")