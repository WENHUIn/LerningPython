## Calculate a server's tip.
bill = float(input("Enter amount of bill: "))
percentage = float(input("Enter percentage tip: "))
tip = (bill * percentage) / 100
print("Tip: ${0:.2f}".format(tip))
