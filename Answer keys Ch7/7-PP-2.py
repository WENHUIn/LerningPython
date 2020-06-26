def main():
    acct = SavingsAccount()
    name = input("Enter person's name: ")
    acct.setName(name)
    print("D = Deposit, W = Withdrawal, Q = Quit")
    request = input("Enter D, W, or Q: ").upper()
    while True:
        if request == 'D':
            amount = float(input("Enter amount to deposit: "))
            acct.makeDeposit(amount)
            print("Balance: ${0:,.2f}".format(acct.getBalance()))
            request = input("Enter D, W, or Q: ").upper()
        elif request == 'W':
            amount = float(input("Enter amount to withdraw: "))
            acct.makeWithdrawal(amount)
            print("Balance: ${0:,.2f}".format(acct.getBalance()))
            request = input("Enter D, W, or Q: ").upper()
        elif request == 'Q':
            print("End of transactions. Have a good day",
                 acct.getName() + '.')
            break
        else:
            request = input("Enter D, W, or Q: ").upper()

class SavingsAccount:
    def __init__(self, name="", balance=0.0):
        self._name = name
        self._balance = balance    
        
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setBalance(self, balance):
        self._balance = balance

    def getBalance(self):
        return self._balance
 
    def makeDeposit(self, amount):
        self._balance += amount

    def makeWithdrawal(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds, transaction denied.")
           
    
main()    
