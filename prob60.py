from euler import allprimes, isPrime
import sys
from itertools import permutations
primes = allprimes(100)
le = len(primes)

pos= [0,1,2,3,4]
p = permutations(pos, 2)
perms = []
for perm in p:
    perms.append(perm)

def check(a,b,c,d,e):
    nums = map(str, [a,b,c,d,e])
    for perm in perms:
        new = nums[perm[0]] + nums[perm[1]]
        if not(isPrime(int(new))):
            return False
    return True


for i in range(le):
    for j in range(i+1, le):
        for k in range(j+1, le):
            for l in range(k+1, le):
                for m in range(l+1, le):
                    if check(primes[i],primes[j],primes[k],primes[l],primes[m]):
                        print primes[i],primes[j],primes[k],primes[l],primes[m]
                        print sum([primes[i],primes[j],primes[k],primes[l],primes[m]])
                        sys.exit()
