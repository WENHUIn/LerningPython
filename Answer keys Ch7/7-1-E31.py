def main():
    ## Calculate a workers weekly pay.
    salary = Wages()
    name = input("Enter person's name: ")
    salary.setName(name)
    hours = float(input("Enter number of hours worked: "))
    salary.setHours(hours)
    wage = float(input("Enter hourly wage: "))
    salary.setWage(wage)
    print("Pay for", salary.getName() + ':', salary.payForWeek())
    
class Wages:
    def __init__(self, name="", hours=0.0, wage=0.0):
        self._name = name
        self._hours = hours    # Number of hours worked during week
        self._wage = wage      # Hourly wage 
        
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setHours(self, hours):
        self._hours = hours

    def getHours(self):
        return self._hours
   
    def setWage(self, wage):
        self._wage = wage

    def getHours(self):
        return self._hours
 
    def payForWeek(self):
        amount = self._hours * self._wage
        if self._hours > 40:
            amount = 40 * self._wage + ((self._hours - 40) *
                     (1.5 * self._wage))
        return "${0:,.2f}".format(amount) 
                                     
main()    
