## Determine class size for which the probability  is greater
## than 50% that someone has the same birthday as you.
num  = 1
while ((364 / 365) ** num) > 0.5:
    num += 1
print("With", num, "students, the probability")
print("is greater than 50% that someone")
print("has the same birthday as you.")
