# Very slow(~19 seconds). Simple Brute Force. Check out alternative in same folder.

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

# get a list of prime factors
# ex: get_prime_factors(140) -> ((2,2), (5,1), (7,1))
#     140 = 2^2 * 5^1 * 7^1
def distinct(n):
    ans =0
    for p in primelist:
        if p>n:
            break
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            ans+=1
        if n==1:
            break
    return ans

primelist = allprimes(100000)[1]


k = 2*3*5*7
consec = 1
while consec<4:
    k+=1
    if distinct(k)==4:
        consec+=1
    else:
        consec = 0


print k-3
