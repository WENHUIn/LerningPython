## Find the GCD of two numbers.
m = int(input("Enter value of M: "))
n = int(input("Enter value of N: "))
while n != 0:
    t = n
    n = m % n    # remainder after m is divided by n
    m = t
print("Greatest common divisor:", m) 

