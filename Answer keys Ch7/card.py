import random

class Card:
    def __init__(self, denomination="", suit=""):
        self._denomination = denomination
        self._suit = suit

    def setDenomination(self, value):
        self._denomination = value
        
    def getDenomination(self):
        return self._denomination

    def setSuit(self, value):
        self._suit = value
        
    def getSuit(self):
        return self._suit

    def selectAtRandom(self):
        denominations = ['2', '3', '4', '5', '6', '7', '8', '9',
                         "10", "jack", "queen", "king", "ace"]
        self._denomination = random.choice(denominations)
        self._suit = random.choice(["spades", "hearts", "clubs", "diamonds"])

    def __str__(self):
        return (self._denomination + " of " + self._suit)
