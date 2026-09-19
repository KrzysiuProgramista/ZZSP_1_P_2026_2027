oceny = [2,4,2,5,7,6]

print("Najwyższa:", max(oceny))
print("Najniższa:", min(oceny))
print("Średnia:", sum(oceny) / len(oceny))

oceny.sort(reverse=True)
print("Po sortowane:", oceny)