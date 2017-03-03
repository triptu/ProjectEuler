import operator as op
mod = 10**9+7

def gcd(a, b):
    if b==0:
        return a;
    else:
        return gcd(b, a%b)

# Fast power
def power(base,n):
    if n==1:
        return base
    elif n%2==0:
        return (power(base, n/2))**2
    else:
        return ((power(base,n/2))**2)*base

# modular exponentiation. pow(base,n,mod)
def modexp(base,n):
    if n==1:
        return base%mod
    elif n%2==0:
        return ((power(base, n/2))**2)%mod
    else:
        return (((power(base,n/2))**2)*base)%mod

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

# for any a,m
def invmod(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

# p should be prime. result follows from fermat's little theorem
def invmodp(n, p):
    global mod
    temp = mod
    mod = p
    return modexp(n, p-2)
    mod = temp

# extended euclid. Find x,y such that ax + by = gcd(a,b). Returns (gcd, x, y)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

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
    # return count, primes
    return primes

# get a list of prime factors
# ex: get_prime_factors(140) -> ((2,2), (5,1), (7,1))
#     140 = 2^2 * 5^1 * 7^1
def get_prime_factors(n, primelist=None):
    if primelist is None:
        count, primelist = allprimes(n)
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
        if n==1:
            break

    return fs


# get a list of all factors for N
# ex: get_factors(10) -> [1,2,5,10]
def get_factors(n, primelist=None):
    if primelist is None:
        count, primelist = allprimes(n)

    fcount = {}
    for p in primelist:
        if p > n:
            break
        if n % p == 0:
            fcount[p] = 0

        while n % p == 0:
            n /= p
            fcount[p] += 1

    factors = [1]
    for i in fcount:
        level = []
        exp = [i**(x+1) for x in range(fcount[i])]
        for j in exp:
            level.extend([j*x for x in factors])
        factors.extend(level)

    return factors

# Count the prime divisors for all the numbers below n. Returns one by one. Use as iterator-
# for number, divisors in count_divisors(n):
def count_divisors(n):
    div = [0] * n
    for i in xrange(2, n):
        if div[i] == 0:
            yield i, 1  # prime number
            for j in xrange(i, n, i):
                div[j] += 1  # add divisor to all multiples
        else:
            yield i, div[i]

# print gcd(5,10)
# print egcd(5, 17)
# print invmod(4, 7)
# print invmodp(4, 7)
# print isPrime(5)
# print get_prime_factors(140)
# print get_factors(10)

