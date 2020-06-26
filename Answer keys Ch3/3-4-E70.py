## Determine when the Steelers first won a Super Bowl game.
num = 0
teams = open("SBWinners.txt", 'r')
for team in teams:
    num += 1
    if team.strip() == "Steelers":
        break
teams.close()
print("The Steelers first won the")
print("Super Bowl in game #" + str(num) + '.')
