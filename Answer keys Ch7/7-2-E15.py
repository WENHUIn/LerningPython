def main():
    ## Calculate the values for an interest-only mortgage.
    principal = float(input("Enter principal of mortgage: "))
    interestRate = float(input("Enter percent interest rate: "))
    term = float(input("Enter duration of mortgage in years: "))
    numberOfInterestOnlyYears = \
                    float(input("Enter number of interest-only years: "))
    mort = InterestOnlyMortgage(principal, interestRate,
                              term, numberOfInterestOnlyYears)
    print("Monthly payment for first {0:.0f} years: ${1:,.2f}".
          format(numberOfInterestOnlyYears, mort.initialMonthlyPayment()))
    mort.setTerm(term - numberOfInterestOnlyYears)
    print("Monthly payment for last {0:.0f} years: ${1:,.2f}".
          format(mort.getTerm(), mort.calculateMonthlyPayment()))
    
class Mortgage:
   def __init__(self, principal, interestRate, term):
       self._principal = principal
       self._interestRate = interestRate
       self._term = term
       
   def calculateMonthlyPayment(self):
       i = self._interestRate / 1200 
       return ((i / (1 - ((1 + i) ** (-12 * self._term)))) 
              * self._principal)

class InterestOnlyMortgage(Mortgage):
    def __init__(self, principal, interestRate,
                 term, numberOfInterestOnlyYears):
        super().__init__(principal, interestRate, term)
        self._numberOfInterestOnlyYears = numberOfInterestOnlyYears

    def initialMonthlyPayment(self):
        return self._principal * (self._interestRate / 1200)

    def setTerm(self, numberOfInterestOnlyYears):
        self._term -= self._numberOfInterestOnlyYears

    def getTerm(self):
        return self._term        

main()







