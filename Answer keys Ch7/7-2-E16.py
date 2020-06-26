import mortgage

def main():
    ## Calculate values for a mortgage with points.
    principal = float(input("Enter principal amount of mortgage: "))
    interestRate = float(input("Enter percent interest rate: "))
    term = float(input("Enter duration of mortgage in years: "))
    numberOfPoints = float(input("Enter number of discount points: "))
    mort = MortgageWithPoints(principal, interestRate,
                              term, numberOfPoints)
    print("Cost of discount points: ${0:,.2f}".\
                    format(mort.calculateCostOfPoints()))
    print("Monthly payment: ${0:,.2f}".format(mort.\
                             calculateMonthlyPayment()))

class Mortgage:
   def __init__(self, principal, interestRate, term):
       self._principal = principal
       self._interestRate = interestRate
       self._term = term
       
   def calculateMonthlyPayment(self):
       i = self._interestRate / 1200 
       return (i / (1 - ((1 + i) ** (-12 * self._term)))) \
              * self._principal

class MortgageWithPoints(Mortgage):
    def __init__(self, principal, interestRate,
                 term, numberOfPoints):
        super().__init__(principal, interestRate, term)
        self._numberOfPoints = numberOfPoints

    def calculateCostOfPoints(self):
        return self._numberOfPoints * (self._principal / 100)

main()







