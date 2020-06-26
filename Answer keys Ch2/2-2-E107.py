## Calculate equivalent CD interest rate for municipal bond rate.
taxBracket = float(input("Enter tax bracket (as decimal): "))
bondRate = float(input("Enter municipal bond interest rate (as %): "))
equivCDrate = bondRate / (1 - taxBracket)
print("Equivalent CD interest rate:", str(round(equivCDrate, 3)) + '%')

