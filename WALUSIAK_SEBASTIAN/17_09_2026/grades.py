grades = [1, 2, 3, 4, 5, 6]

highest = max(grades)
lowest = min(grades)
length = len(grades)
grades_sum = sum(grades)

print(grades_sum / length)
print(f"the biggest grade is {highest}")
print(f"the lowest grade is {lowest}")
grades_sorted = sorted(grades, reverse=True)

print(grades_sorted)
