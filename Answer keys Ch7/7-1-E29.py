import fraction

def main():
    ## Convert a decimal number to a fraction.
    decimal = input("Enter a positive decimal number less than 1: ")
    decimal = decimal[1:]     # Strip off decimal point.
    f = fraction.Fraction()
    f.setNumerator(int(decimal))
    f.setDenominator(10 ** len(decimal))
    f.reduce()
    msg = "Converted to fraction:"
    print(msg, str(f.getNumerator()) + '/' + str(f.getDenominator()))

main()

