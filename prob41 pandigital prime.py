from itertools import permutations

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

nums = list('1234567')

permsiter = permutations(nums, 7)
perms =[]
for k in permsiter:
    perms.append(k)
perms = perms[::-1]

for k in perms:
    new = int("".join(k))
    if isPrime(new):
        print new
        break
