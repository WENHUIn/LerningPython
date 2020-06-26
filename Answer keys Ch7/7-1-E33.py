import random
import pCard

def main():
   deckOfCards = []
   ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
            "10", "jack", "queen", "king", "ace"]
   suits = ["spades", "hearts", "clubs", "diamonds"]
   for i in ranks:
       for j in suits:
           c = pCard.PlayingCard(i, j)
           deckOfCards.append(c)
   pokerHand = random.sample(deckOfCards, 5)
   pokerHand.sort(key=lambda x: x.getRank())
   for k in pokerHand:
       print(k)

main()       

