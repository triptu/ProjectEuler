from euler import allprimes

primes = allprimes(100000)
primes = primes[1:] # removing 2
k = 9
flag=1
while flag==1:
    for prime in primes:
        if prime>k:
            flag = 0
            break
        diff = (k-prime)/2
        if int(diff**0.5)**2 == diff:
            break
    k+=2
print k-2
