# Primes from 1 to n usig sieve of erastothenes
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

def get_prime_factors(n):
    fs = []
    for p in primelist:
        if p>n:
            break
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            fs.append((p, count))
    return fs

def sumofFactors(n):
    primes = get_prime_factors(n)
    tot=1
    for f in primes:
        tot*= ((f[0]**(f[1]+1)-1)/(f[0]-1))
    return tot-n

# Precalculate all primes till 10001
primelist = allprimes(10001)[1]
d= [0]*10001

# Precalculate sum of factors for all numbers
for i in range(2,10001):
    # d[i] = sum(get_factors(i, primelist)[:-1])
    d[i] = sumofFactors(i)

tot = 0
for k in range(2,10001):
    # Avoiding perfect numbers and recounting
    if d[k]<=10000 and d[d[k]]==k and d[k]>k:
        tot+=k+d[k]
    # for j in range(k+1, 10001):
    #     if d[k]==j and d[j]==k:
    #         tot+=j+k
print tot

