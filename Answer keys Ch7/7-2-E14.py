import mortgage

def main():
    ## Calculate the monthly payment for a mortgage.
    principal = float(input("Enter principal of mortgage: "))
    interestRate = float(input("Enter percent interest rate: "))
    term = float(input("Enter duration of mortgage in years: "))
    mort = mortgage.Mortgage(principal, interestRate, term)
    print("Monthly payment: ${0:,.2f}".format(mort.calculateMonthlyPayment()))   

main()

#### mortgage.py    
##class Mortgage:
##   def __init__(self, principal, interestRate, term):
##       self._principal = principal
##       self._interestRate = interestRate
##       self._term = term
##       
##   def calculateMonthlyPayment(self):
##       i = self._interestRate / 1200 
##       return (i / (1 - ((1 + i) ** (-12 * self._term)))) \
##              * self._principal





