## Calculate a person's lifetime earnings.
name = input("Enter name: ")
age = int(input("Enter age: "))
salary = float(input("Enter starting salary: "))
earnings = 0
for i in range(age, 65):
    earnings += salary
    salary += .05 * salary
print("{0} will earn about ${1:,.0f}.".format(name, earnings)) 
