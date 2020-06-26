## Make change for a purchase of apples.
weight = float(input("Enter weight in pounds: "))
payment = float(input("Enter payment in dollars: "))
cost = (2.5 * weight)
if payment >= cost:
    change = payment - cost
    print("Your change is ${0:,.2f}.".format(change))
else:
    amountOwed = cost - payment
    print("You owe ${0:,.2f} more.".format(amountOwed))
