## Use APYs to compare interest rates offered by two banks.
r1 = float(input("Enter annual rate of interest for Bank 1: "))
m1 = float(input("Enter number of compounding periods for Bank 1: "))
r2 = float(input("Enter annual rate of interest for Bank 2: "))
m2 = float(input("Enter number of compounding periods for Bank 2: "))
ipp1 = r1 / (100 * m1)  # interest rate per period
ipp2 = r2 / (100 * m2)
apy1 = ((1 + ipp1) ** m1) - 1
apy2 = ((1 + ipp2) ** m2) - 1
print("APY for Bank 1 is {0:,.3%}".format(apy1))
print("APY for Bank 2 is {0:,.3%}".format(apy2))
if (apy1 == apy2):
    print("Bank 1 and Bank 2 are equally good.")
else:
    if (apy1 > apy2):
        betterBank = 1
    else:
        betterBank = 2
    print("Bank", betterBank, "is the better bank.") 
