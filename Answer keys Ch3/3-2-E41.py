## Bestow graduation honors.
# Request grade point average.
gpa = eval(input("Enter your grade point average (2 through 4): "))
# Validate GPA between 2 and 4. 
if not (2 <= gpa <=4):
    print("Invalid grade point average. GPA must be between 2 and 4.")
else:
    # Determine if honors are warranted and display conclusion.
    if gpa >= 3.9:
        honors = " summa cum laude."
    elif gpa >= 3.6:
        honors = " magna cum laude."
    elif gpa >= 3.3:
        honors = " cum laude."
    else:
        honors = "."
    print("You graduated" + honors) 
