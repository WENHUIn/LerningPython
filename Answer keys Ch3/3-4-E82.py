## Count the sum of the digits in the first million positive integers.
sum = 0
for i in range(1, 1000001):
    strNum = str(i)
    for j in range(len(strNum)):
        sum += int(strNum[j])
print("The sum of the digits in the numbers")
print("from 1 to one million is {0:,d}.".format(sum))
