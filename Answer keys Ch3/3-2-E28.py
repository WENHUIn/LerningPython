## Determine the cost of copies.
numberOfcopies = int(input("Enter number of copies: "))
if numberOfcopies < 100:
    cost = .05 * numberOfcopies
else:
    cost = 5 + 0.03 * (numberOfcopies - 100)
print("Cost is ${0:,.2f}.".format(cost))
