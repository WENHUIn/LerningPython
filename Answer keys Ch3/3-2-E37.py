## Convert military time to regular time.
militaryTime = input("Enter a military time (0000 to 2359): ")
hours = int(militaryTime[0:2])
minutes = militaryTime[2:4]
if hours >= 12:
    cycle = "pm"
    hours %= 12
else:
    cycle = "am"
if hours == 0:
     hours = 12
print("The regular time is {0}:{1} {2}.".format(hours, minutes, cycle)) 
