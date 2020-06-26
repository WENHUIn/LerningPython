## Calculate a median.
howMany = int(input("How many numbers would you like to enter? "))
listOfNumbers = []
for i in range(howMany):
    num = int(input("Enter a number: "))
    listOfNumbers.append(num)
listOfNumbers.sort()    
if howMany % 2 == 1:
    median = listOfNumbers[int(howMany / 2)]
else:
    m = int(howMany / 2)
    median = (listOfNumbers[m - 1] + listOfNumbers[m]) / 2    
print("Median:", median)
