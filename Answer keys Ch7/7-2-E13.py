class Mortgage:
    def __init__(self, principal, interestRate, term):
        self._principal = principal
        self._interestRate = interestRate
        self._term = term
       
    def calculateMonthlyPayment(self):
        i = self._interestRate / 1200 
        return ((i / (1 - ((1 + i) ** (-12 * self._term)))) 
               * self._principal)
      
main()







