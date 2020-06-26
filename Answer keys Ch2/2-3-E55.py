## Calculate a new salary.
beginningSalary = float(input("Enter beginning salary: "))
raisedSalary = 1.1 * beginningSalary
cutSalary = .9 * raisedSalary
percentChange = (cutSalary - beginningSalary) / beginningSalary
print("New salary: ${0:,.2f}".format(cutSalary))
print("Change: {0:.2%}".format(percentChange))
