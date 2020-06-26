def main():
    ## Simulate a toll booth cash register.
    device = Register()
    carryOn = 'Y'
    while carryOn.upper() == 'Y':
        vehicle = input("Enter type of vehicle (car/truck): ")
        if vehicle == "car":
            device.ProcessCar()
        else:
            device.ProcessTruck()
        print("Number of vehicles:", device.getCount())
        print("Money Collected: ${0:,.2f}".format(device.getTally()))
        carryOn = input("Do you want to enter more vehicles (Y/N)? ")
    print("Have a good day.")
        
    
class Register:
    def __init__(self, count=0, tally=0):
        self._count = count
        self._tally = tally
        
    def setCount(self, count):
        self._count = count

    def setTally(self, tally):
        self._tally = tally

    def getCount(self):
        return self._count

    def getTally(self):
        return self._tally

    def ProcessCar(self):
        self._count += 1    
        self._tally += 1  # Cost is $1 per car.
      
    def ProcessTruck(self):
        self._count += 1    
        self._tally += 2  # Cost is $2 per truck.
            
main()    
