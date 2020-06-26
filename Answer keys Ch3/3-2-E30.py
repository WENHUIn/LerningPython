## Determine weekly pay (including overtime pay).
wage = float(input("Enter hourly wage: "))
hours = float(input("Enter number of hours worked: "))
if hours <= 40:
    grossPay = wage * hourse
else:
    grossPay = (wage * 40) + (1.5 * wage * (hours - 40))
print("Gross pay for week is ${0:,.2f}.".format(grossPay))
