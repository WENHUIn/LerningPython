import pairOfDice

def main():
    ## Estimate the Chevalier de Méré probability.
    numberOfSuccesses = 0
    for i in range(10000):
        if playGame():
            numberOfSuccesses += 1
    print(numberOfSuccesses / 10000)

def playGame():
    doubleSixes = False
    dice = pairOfDice.PairOfDice()
    for i in range(24):
        dice.roll()
        if dice.sum() == 12:
            doubleSixes = True
    return doubleSixes            
        
main()

                                      
    
