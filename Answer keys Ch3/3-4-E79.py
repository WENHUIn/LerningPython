## Identify president by number.
infile = open("USpres.txt", 'r')
for i in range(15):
    infile.readline()
print("The 16th president was")
print(infile.readline().rstrip() + '.')
infile.close()
