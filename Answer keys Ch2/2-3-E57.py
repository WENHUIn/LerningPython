## Calculate a future value.
p = float(input("Enter principal: "))
r = float(input("Enter interest rate (as %): "))
n = int(input("Enter number of years: "))
futureValue = p * (1 + (r / 100)) ** n
print("Future value: ${0:,.2f}".format(futureValue))

      
             
