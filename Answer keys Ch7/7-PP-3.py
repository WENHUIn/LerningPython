def main():
    ## Create a payroll summary.
    listOfEmployees = createListOfEmployees()
    displayResults(listOfEmployees)
    
def createListOfEmployees():
    listOfEmployees = []
    carryOn = 'Y'
    while carryOn == 'Y':
        name = input("Enter employees's name: ")
        prompt = "Enter employee's classification (Salaried or Hourly): "
        classification = input(prompt) 
        hours = float(input("Enter the number of hours worked: "))
        if classification.upper() == "SALARIED":
            rate = float(input("Enter weekly salary: "))
            person = SalariedEmployee(name, rate, hours)
        else:
            rate = float(input("Enter hourly wage: "))
            person = HourlyEmployee(name, rate, hours)
        listOfEmployees.append(person)    
        carryOn = input("Do you want to continue (Y/N)? ")
        carryOn = carryOn.upper()
    return listOfEmployees

def displayResults(listOfEmployees):
    print()
    numberOfSalariedEmployees = 0
    totalPayroll = 0.0
    totalHoursWorked = 0.0
    for person in listOfEmployees:
        print("{0:s}: ${1:,.2f}".format(person.getName(),
                                        person.calculatePay()))
    for person in listOfEmployees:
        totalHoursWorked += person.getHoursWorked()
        if isinstance(person, SalariedEmployee):
            numberOfSalariedEmployees += 1
        totalPayroll += person.calculatePay()               
    print("Number of employees:", len(listOfEmployees))
    print("Number of salaried employees:", numberOfSalariedEmployees)
    print("Total payroll: ${0:,.2f}".format(totalPayroll))
    average = "Average number of hours worked per employee: {0:.2f}"
    print(average.format(totalHoursWorked / len(listOfEmployees)))

class Employee:
    def __init__(self, name="", rate=0.0, hoursWorked=0.0):
        self._name = name
        self._rate = rate
        self._hoursWorked = hoursWorked

    def setName(self, name):
        self._name = name
        
    def getName(self):
        return self._name

    def setRate(self, rate):
        self._rate = rate
        
    def getRate(self):
        return self._rate

    def setHoursWorked(self, hoursWorked):
        self._hoursWorked = hoursWorked
        
    def getHoursWorked(self):
        return self._hoursWorked
        
class SalariedEmployee(Employee):
    
    def calculatePay(self):
        return self._rate

class HourlyEmployee(Employee):

    def calculatePay(self):
        return self._hoursWorked * self._rate
            
main()


