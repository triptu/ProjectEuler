from itertools import permutations
from euler import isPrime

for i in range(1000, 9999):
    if not(isPrime(i)):
        continue
    perm = permutations(str(i), 4)
    perms = []
    for p in perm:
        num = int("".join(p))
        if isPrime(num) and num not in perms:
            perms.append(num)
    for j in perms:
        if j<=i:
            continue
        for k in perms:
            if k<=j:
                continue
            if (i+k)/2 == j:
                print i,j,k
