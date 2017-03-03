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

# Primes from 1 to n
def allprimes(n):
    sieve = [1]*(n+1)
    sieve[0]=sieve[1]=0
    primes = []
    for pos, k in enumerate(sieve):
        if k==0:
            continue
        primes.append(pos)
        for j in range(pos*pos, n+1, pos):
            sieve[j] = 0
    return primes

primelist= allprimes(100000)
primes = {}

l = len(primelist)
prefSum=[0]*(l+1)
prefSum[0]= primelist[0]
for i in range(1, l):
    prefSum[i] = prefSum[i-1]+primelist[i]
prefSum[-1] = 0

maxcount = 0
maxPrime = 0
for left in range(l):
    for right in range(left+maxcount+1, l):
        Sum = prefSum[right] - prefSum[left-1]  # Sum of that range
        if Sum>1000000:
            break
        if isPrime(Sum):
            maxcount = right-left
            maxPrime = Sum

print maxPrime
