## Bestow graduation honors.
# Request grade point average.
gpa = eval(input("Enter your gpa: "))
# Determine if honors are warranted.
if gpa >= 3.9:
    honors = " summa cum laude."
if 3.6 <= gpa < 3.9:
    honors = " magna cum laude."
if (3.3 <= gpa < 3.6):
    honors = " cum laude."
if gpa < 3.3:
    honors = "."
# Display conclusion.
print("You graduated" + honors)
