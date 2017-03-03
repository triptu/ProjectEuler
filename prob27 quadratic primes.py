def isPrime(n):
    if n==2 or n==3:
        return True
    if n<=1 or n%2==0 or n%3==0:
        return False
    if n%6!=1 and n%6!=5:   # Prime numbers > 3 are in form of 6k +/- 1.
        return False
    sqr = int(n**0.5 + 0.5)
    for i in range(5, sqr+1, 6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

Max, count = 0, 0
A, B = 0, 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n=0
        count = 0
        while True:
            new = n**2 + a*n + b
            if not(isPrime(new)):
                break
            n+=1
            count+=1
        if count>Max:
            Max = count
            A,B = a, b

print "Max primes achievable =", Max
print "For a =",A," and b =", B
print "ab =", A*B
