## Process a savings account withdrawal.
balance = float(input("Enter current balance: "))
amountOfWithdrawal = float(input("Enter amount of withdrawal: "))
if (balance >= amountOfWithdrawal):
    balance -= amountOfWithdrawal
    print("The new balance is ${0:,.2f}.".format(balance))
    if balance < 150:
        print("Balance below $150", "Warning")
else:
    print("Withdrawal denied.")

