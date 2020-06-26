## Second-Suit Half-Off Sale
cost1 = float(input("Enter cost of first suit: "))
cost2 = float(input("Enter cost of second suit: "))
twoCosts = [cost1,  cost2]
cost = max(twoCosts) + (.5 * min(twoCosts))
print("Cost of the two suits is ${0:.2f}".format(cost))
