grades = [6, 7, 8, 9, 2, 5]
highest = max(grades)
lowest = min(grades)
average = sum(grades) / len(grades)

grades.sort(reverse=True)

print("Highest grade:", highest)
print("Lowest grade:", lowest)
print("Average grade:", average)
print("Grades best to worst:", grades)
