## Calculate balances in an increasing annuity.
print("         BALANCE AT")
print("YEAR    ", "END OF YEAR")   
balance = 0
year = 2014
for i in range(1, 61):
    balance = 1.0025 * balance + 100
    if i % 12 == 0:
        print(year, "    ${0:,.2f}".format(balance))
        year += 1



  

