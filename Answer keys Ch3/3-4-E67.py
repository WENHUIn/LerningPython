## Compare two salary options.
# Calculate amount earned in ten years with Option 1.
salary = 20000
option1 = 0
for i in range(10):
    option1 += salary
    salary += 1000
print("Option1 earns ${0:,d}.".format(option1))
# Calculate amount earned in ten years with Option 2.
salary = 10000
option2 = 0
for i in range(20):
    option2 += salary
    salary += 250
print("Option2 earns ${0:,d}.".format(option2))
