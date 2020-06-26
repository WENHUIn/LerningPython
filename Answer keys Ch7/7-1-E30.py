import fraction

def main():
    ## Add two fractions.
    f1 = fraction.Fraction()
    numerator = int(input("Enter numerator of first fraction: "))
    f1.setNumerator(numerator)
    denominator = int(input("Enter denominator of first fraction: "))
    f1.setDenominator(denominator)
    f2 = fraction.Fraction()
    numerator = int(input("Enter numerator of second fraction: "))
    f2.setNumerator(numerator)
    denominator = int(input("Enter denominator of second fraction: "))
    f2.setDenominator(denominator)
    print("Sum:", calculateSum(f1, f2))

def calculateSum(f1, f2):
    # Note: a/b + c/d = (ad + bc)/bd
    sum = fraction.Fraction()
    sum.setDenominator(f1.getDenominator() * f2.getDenominator())
    sum.setNumerator((f1.getNumerator() * f2.getDenominator()) +
                     (f1.getDenominator() * f2.getNumerator())) 
    sum.reduce()
    if sum.getDenominator() != 1:
        return  str(sum.getNumerator()) + '/' + str(sum.getDenominator())
    else:
        return sum.getNumerator()
    
main()

