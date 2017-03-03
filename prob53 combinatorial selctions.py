from euler import ncr

limit = 1000000

c=0
for n in range(1,101):
    for r in range(1, n+1):
        if ncr(n, r)>limit:
            c+=1
print c
