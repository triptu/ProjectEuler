from euler import allprimes, isPrime
from itertools import combinations

primes = allprimes(200000)
nums = list('0123456789')
flag =0
for prime in primes:
    p = str(prime)
    if len(p)==len(set(p)): # All distinct digits.
        continue
    count = 0
    num = 0
    warn = 0
    for i in range(10):
        num = nums[i]
        if p.count(num)>1:
            if warn<=0:
                warn += 1
                continue
            break
    # pos = []
    # for i in range(len(p)):
    #     if p[i]==num:
    #         pos.append(i)
    # for k in range(1, len(pos)+1):
    #     combs = combinations(pos, k)
    #     for comb in combs:
    #         for j in range(10):
    #             new = ''
    #             count = 0
    #             for i in range(len(p)):
    #                 if i in pos:
    #                     new+=str(j)
    #                 else:
    #                     new+=p[i]
    #             # print new
    #             if isPrime(int(new)):
    #                 count+=1
    #         if count>=8:
    #             print prime, comb
    #             flag = 1
    #             break
    #     if flag==1:
    #         break
    # if flag==1:
    #     break
