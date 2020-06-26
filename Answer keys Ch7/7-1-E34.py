import random
import pCard

def main():
    ## Display a bridge hand.
    deckOfCards = []
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
             "10", "jack", "queen", "king", "ace"]
    suits = ["spades", "hearts","diamonds", "clubs"]
    for i in ranks:
        for j in suits:
            c = pCard.PlayingCard(i, j)
            deckOfCards.append(c)
    bridgeHand = random.sample(deckOfCards, 13)
    bridgeHand.sort(key=lambda x: x.getSuit(), reverse=True)
    for k in bridgeHand:
        print(k)

main()       

