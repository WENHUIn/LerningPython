## Prime factorization
lstFactors = []
n = int(input("Enter a positive integer (> 1): "))
f = 2
while n > 1:
    if n // f == n / f:    # true if f divides n
        lstFactors.append(str(f))
        n = n // f
    else: 
        f += 1
result = "  ".join(lstFactors)        
print("Prime factors are", result)
