## Calculate a tip.
bill = float(input("Enter amount of bill: "))
tip = bill * 0.15
if (tip < 2):
    tip = 2
print("Tip is ${0:,.2f}".format(tip))
