## Determine the monthly payment for a car loan.
loanAmount = float(input("Enter amount of loan: "))
interestRate = float(input("Enter interest rate (%): "))
numYears = float(input("Enter number of years: "))
i = interestRate / 1200
monthlyPayment = (i / (1 - ((1 + i) ** (-12 * numYears)))) * loanAmount
print("Monthly payment: ${0:,.2f}".format(monthlyPayment))
