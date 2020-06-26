## Calculate a present value.
f = float(input("Enter future value: "))
r = float(input("Enter interest rate (as %): "))
n = int(input("Enter number of years: "))
presentValue = f / ((1 + (r / 100)) ** n)
print("Present value: ${0:,.2f}".format(presentValue))

      
             
