## Analyze a car loan.
p = eval(input("Enter the amount of the loan: "))
a = eval(input("Enter the interest rate: "))
n = int(input("Enter the duration in months: "))
r = a / 1200
monthlyPayment = (p * r) / (1 - (1 + r) ** (-n))
monthlyPayment = round(monthlyPayment, 2)
print("Monthly Payment: ${0:,.2f}".format(monthlyPayment))
totalInterest = n * monthlyPayment - p
print("totalInterestPaid: ${0:,.2f}".format(totalInterest))
