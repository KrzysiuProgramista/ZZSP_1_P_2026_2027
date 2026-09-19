week = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print(week[0:5])
print(week[5:7])
week.reverse()
print(week)
# pop(idx) : Removes by INDEX. Returns the removed item. (Defaults to last item).
# remove(val): Removes by VALUE. Deletes the first match only. Returns None.
# del[idx]   : Removes by INDEX/SLICE. Supports range slices. Returns None.