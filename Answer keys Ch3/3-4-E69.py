## Determine the number of Super Bowl wins for the Pittsburg Steelers.
teams = open("SBWinners.txt", 'r')
numberOfWins  = 0
for team in teams:
    if team.rstrip() == "Steelers":
        numberOfWins  += 1
print("The Steelers won")
print(numberOfWins , "Super Bowl games.")
