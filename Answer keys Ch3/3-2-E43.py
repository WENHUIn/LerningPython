## Calculate a person's state income tax.
income = float(input("Enter your taxable income: "))
if income <= 20000:
    tax = .02 * income
else:
    if income <= 50000:
        tax = 400 + .025 * (income - 20000)
    else:
        tax = 1150 + .035 * (income - 50000)
print("Your tax is ${0:,.0f}.".format(tax))
