## Calculate average of best two of three grades.
grades = []
for i in range(3):
    grade = int(input("Enter a grade: "))
    grades.append(grade)
grades.sort()
average = (grades[1] + grades[2]) / 2
print("Average: {0:n}".format(average))
