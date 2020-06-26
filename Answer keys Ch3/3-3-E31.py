## Maintain a savings account.
print("Options:")
print("1. Make a Deposit")
print("2. Make a Withdrawal")
print("3. Obtain Balance")
print("4. Quit")
balance = 1000
while True:
    num = int(input("Make a selection from the options menu: "))
    if num == 1:
        deposit = float(input("Enter amount of deposit: "))
        balance += deposit
        print("Deposit Processed.")
    elif num == 2:
        withdrawal = float(input("Enter amount of withdrawal: "))
        while (withdrawal > balance):
            print("Denied. Maximum withdrawal is ${0:,.2f}"
                   .format(balance))
            withdrawal = float(input("Enter amount of withdrawal: "))
        balance -= withdrawal
        print("Withdrawal Processed.")
    elif num == 3:
        print("Balance: ${0:,.2f}".format(balance))
    elif num == 4:
        break
    else:
        print("You did not enter a proper number.")
