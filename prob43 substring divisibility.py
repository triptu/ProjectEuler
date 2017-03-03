from itertools import permutations

digits = map(int, list('0123456789'))
perms = permutations(digits, 10)
primes= [2,3,5,7,11,13,17]
ans = 0
for p in perms:
    k = 2
    while k<=8:
        num = p[k-1]*100 + p[k]*10 + p[k+1]
        if num%(primes[k-2])!=0:
            break
        k+=1
    else:
        p2 = map(str, p)
        n = int("".join(p2))
        print n
        ans+=n

print ans
