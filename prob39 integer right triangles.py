memo = {}

for a in range(1, 1000):
    for b in range(a,1000):
        c = int((a**2 + b**2)**0.5 + 0.5)
        if a+b+c>1000:
            break
        if a**2+b**2 != c**2:
            continue
        p = a+b+c
        if p in memo:
            memo[p]+=1
        else:
            memo[p]=1

ans = 0
count = 0
for key in memo:
    if memo[key]>count:
        count = memo[key]
        ans = key

print ans, count
