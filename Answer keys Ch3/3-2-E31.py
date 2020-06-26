## Calculate an average after dropping the lowest score.
scores = []
scores.append(eval(input("Enter first score: ")))
scores.append(eval(input("Enter second score: ")))
scores.append(eval(input("Enter third score: ")))
scores.remove(min(scores))
average = sum(scores) / 2
print("Average of the two highest scores is {0:.2f}".format(average))
