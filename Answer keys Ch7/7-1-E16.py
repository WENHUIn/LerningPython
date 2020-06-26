import pairOfDice

def main():
    ## Play a game of dice.
    dice1 = pairOfDice.PairOfDice()
    dice1.roll()
    print("Player 1:", dice1.sum())
    dice2 = pairOfDice.PairOfDice()
    dice2.roll()
    print("Player 2:", dice2.sum())
    if dice1.sum() == dice2.sum():
        print("TIE")
    elif dice1.sum() > dice2.sum():
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
    
main()    
