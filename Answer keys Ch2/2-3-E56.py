## Calculate a change in salary.
beginningSalary = float(input("Enter beginning salary: "))
raisedSalary = 1.05 * 1.05 * 1.05 * beginningSalary
percentChange = (raisedSalary - beginningSalary) / beginningSalary
print("New salary: ${0:,.2f}".format(raisedSalary))
print("Change: {0:.2%}".format(percentChange))

