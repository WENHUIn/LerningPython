## Values of a decreasing annuity.
balance = float(input("Enter amount of deposit: "))
interestMultiplier = 1.003   # multiplier due to interest
monthlyWithdrawal = 600
month = 0
while balance > 600:
    balance = (interestMultiplier * balance) - monthlyWithdrawal
    month += 1
print("Balance will be ${0:,.2f} \nafter {1} months.".format(balance, month))
