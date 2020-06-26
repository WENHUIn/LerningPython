## Find a special number.
for num in range(1000, 10000):
    list1 = list(str(num))
    list1.reverse()
    revNum = int("".join(list1))
    if revNum == 4 * num:
        break
print("Since 4 times", num, "is", str(revNum) + ',')
print("the special number is", str(num) + '.')
