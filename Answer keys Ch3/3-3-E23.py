## Determine when a car loan will be half paid off.
principal = 15000
balance = principal     # initial balance
monthlyPayment = 290
monthlyFactor = 1.005   # multiplier due to interest
month = 0
while(balance >= principal / 2):
    balance =  (monthlyFactor * balance) - monthlyPayment
    month += 1
print("Loan will be half paid \noff after", month, "months.")
