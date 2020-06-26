import fraction

def main():
    ## Reduce a specified fraction to lowest terms.
    f = fraction.Fraction()
    numerator = int(input("Enter numerator of fraction: "))
    f.setNumerator(numerator)
    denominator = int(input("Enter denominator of fraction: "))
    f.setDenominator(denominator)
    f.reduce()
    msg = "Reduction to lowest terms:"
    if f.getDenominator() != 1:
        print(msg, str(f.getNumerator()) + '/' + str(f.getDenominator()))
    else:
        print(msg, f.getNumerator())

main()        

     


