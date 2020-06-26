## Determine cost of bagels.
num = int(input("Enter number of bagels: "))
if num < 6:
    cost = 0.75 * num
else:
    cost = 0.6 * num
print("Cost is ${0:,.2f}.".format(cost))
