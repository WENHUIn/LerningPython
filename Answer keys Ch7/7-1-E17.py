import pairOfDice

def main():
    numberOfSevens = 0
    for i in range(100000):
        dice = pairOfDice.PairOfDice()
        dice.roll()
        if dice.sum() == 7:
            numberOfSevens += 1
    print("7 occurred {0:.2%} of the time.".format(numberOfSevens / 100000))        
                                      
main()    

#### pairOfDice.py
##import random
##
##class PairOfDice:
##    def __init__(self):
##        self._redDie = 0
##        self._blueDie = 0
##        
##    def getRedDie(self):
##        return self._redDie
##
##    def getBlueDie(self):
##        return self._blueDie
##
##    def roll(self):
##        self._redDie = random.choice(range(1, 7))
##        self._blueDie = random.choice(range(1, 7))
##        
##    def sum(self):
##        return self._redDie + self._blueDie
