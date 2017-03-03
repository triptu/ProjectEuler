from time import time
start = time()

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
    count = 0
    sieve[0]=sieve[1]=0
    primes = []
    for pos, k in enumerate(sieve):
        if k==0:
            continue
        count+=1
        primes.append(pos)
        for j in range(pos*pos, n+1, pos):
            sieve[j] = 0
    return count, primes

primes = allprimes(1000000)[1]
count = 0
for prime in primes:
    p = str(prime)
    l = len(p)
    for k in range(l):
        new = p[k:] + p[0:k]
        if not(isPrime(int(new))):
            break
    else:
        count+=1

print "Time -", time()- start,"seconds."
print count
