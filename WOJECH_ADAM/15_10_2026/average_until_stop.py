ct = 0
tot = 0

while True:
    imp = input("enter a number (or 'stop' to finish): ")

    if imp.lower() == "stop":
        break

    num = float(imp)
    tot += num
    ct += 1

print("numbers entered:", ct)

if ct > 0:
    aver = tot / ct
    print("average:", aver)
else:
    print("no numbers were entered.")