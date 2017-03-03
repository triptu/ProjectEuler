from time import time
start = time()

limit = 1000
Max = 0
num = 0
'''Approach-  1/7 first find 10%7=3 then find 30%7=2, then 20%7=6, 60%7=4, 40%7=5, 50%7=1.
   Now things are going to repeat as this remainder has already occured.
   We will only check prime numbers. Because of fermat's little theorem, a prime number can have
   at max p-1 recurring decimals. We have to basically find the highest prime number having this much
   cycle.
'''
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

for i in allprimes(limit)[1][::-1]:
    curr = 10%i
    remainders = []
    count = 0
    while curr not in remainders:
        remainders.append(curr)
        curr = (curr*10)%i
        count+=1
    if count>Max:
        Max = count
        num = i
    if count==i-1:
        break

print "Time taken -", time()-start,"seconds."
print "Maximum recurring cycles ", Max
print "For the number ", num
