import pCard

def main():
    c = pCard.PlayingCard()
    c.selectAtRandom()
    c.setSuit("diamonds")
    print(c)
 
main()
