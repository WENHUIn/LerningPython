## Determine the real roots of a quadratic equation
## of the form ax**2 + bx +c = 0.
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
# Test that first coefficient is nonzero.
if a == 0:
    print("a must be non-zero.")
else:
    # Determine solution
    delta = b ** 2 - (4 * a * c)
    if delta < 0:     # no real solutions
        print("No real solutions")
    elif delta == 0:  # one real solution
        sol = -b / (2 * a)
        if int(sol) == sol:
            print("Solution: {0:,.0f}".format(sol))
        else:
            print("Solution: {0:,.4f}".format(sol))
    else:             # two real solutions
        sol1 = (-b + (delta ** 0.5)) / (2 * a)
        sol2 = (-b - (delta ** 0.5)) / (2 * a)
        if int(sol1) == sol1 and int(sol2) == sol2:
            print("Solutions: {0:,.0f} and {1:,.0f}".format(sol1, sol2))
        else:    
            print("Solutions: {0:,.4f} and {1:,.4f}".format(sol1, sol2))
