## Analyze Rule of 72.
print("\t\tRule of 72")
print("Interest\tDoubling Time\tActual Doubling")
print("Rate\t\t(in years)\tTime (in years)")
for i in range(1,21):
    amount = 100
    years = 0
    while amount < 200:
        amount *= 1 + (i / 100)
        years += 1
    print(str(i) + '%' + "\t\t" +  str(72 // i) + "\t\t"+ str(years))


