import random

class PairOfDice:
    def __init__(self):
        self._redDie = 0
        self._blueDie = 0
        
    def getRedDie(self):
        return self._redDie

    def getBlueDie(self):
        return self._blueDie

    def roll(self):
        self._redDie = random.choice(range(1, 7))
        self._blueDie = random.choice(range(1, 7))
        
    def sum(self):
        return self._redDie + self._blueDie
                                      
    
