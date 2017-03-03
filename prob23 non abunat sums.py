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


primelist = allprimes(28123)[1]
abun = []
for k in range(12, 28124):
    temp = sumofFactors(k)
    if temp>k:
        abun.append(k)

nums = [0]*28124
l = len(abun)
for i in range(l):
    for j in range(i, l):
        new = abun[i]+abun[j]
        if new>28123:
            break
        nums[new] =1

tot = 0
for k in range(len(nums)):
    if nums[k]==0:
        tot+=k
print tot
