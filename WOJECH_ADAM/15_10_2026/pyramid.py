hg = int(input("enter the pyramid height: "))

for i in range(hg):
    spc = hg - i - 1
    sta = 2 * i + 1

    print(" " * spc + "*" * sta)