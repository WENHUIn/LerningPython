import random

class PlayingCard:
    def __init__(self, rank="queen", suit="hearts"):
        self._rank = rank
        self._suit = suit

    def setRank(self, rank):
        self._rank = rank

    def setSuit(self, suit):
        self._suit = suit

    def getRank(self):
        return self._rank

    def getSuit(self):
        return self._suit
    
    def selectAtRandom(self):
        ## Randomly select a rank and a suit.
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
                 "10", "jack", "queen", "king", "ace"]
        self._rank = random.choice(ranks)
        self._suit = random.choice(["spades", "hearts", "clubs", "diamonds"])

    def __str__(self):
        return(self._rank + " of " + self._suit)
