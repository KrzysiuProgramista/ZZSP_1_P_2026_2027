week = ["monday", "tuesday", "wendsday", "thursday", "friday", "saturday", "sunday"]

working_days = slice(0, 5)
weekend = slice(5,7)

print("working days are", week[working_days])
print("weekend days are", week[weekend])
week_reversed = week[::-1]
print(week_reversed)

#remove() deletes list items by telling its name for example remove("monday")
#pop() deletes list items by telling its index and allows to use it later for example pop(1)
#del allows us to delete whole list and can delets items by index for example del week
