## Display the balances on a car loan.
print("         AMOUNT OWED AT")
print("YEAR    ", "END OF YEAR")   
balance = 15000
year = 2012
for i in range(1, 49):
    balance = 1.005 * balance - 290
    if i % 12 == 0:
        year += 1
        print(year, "    ${0:,.2f}".format(balance))
print(year + 1, "    $0.00")    

