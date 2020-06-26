## Analyze grades on a final exam.
infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0    # number of grades above average
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grades above average: {0:.2f}%"
      .format(100 * num / len(grades)))        
