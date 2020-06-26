## Calculate the cost of widgets.
num = int(input("Enter number of widgets: "))
if num < 100:
    cost = num * 0.25
else:
    cost = num * 0.20
print("Cost is ${0:,.2f}".format(cost))


