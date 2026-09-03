name = input("What is your name? ")
age = input("How old are you? ")
home = input("What is your home town? ")

print("Name:", name)
print("Age:", age)
print("Home town:", home)

# sep is a optional keyword argument that handles spacing betweens items in a print statement
# end is a optional keyword argument that handles what is printed at the end of a print statement

# ex

print(name, age, home, sep=", ", end=".\n")
# - adrian, 15, zgierz.
