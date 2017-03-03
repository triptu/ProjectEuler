def ds(n):
    new = str(n)
    ans = 0
    for k in new:
        ans += int(k)
    return ans

m= 0
for a in range(1,100):
    for b in range(1,100):
        num = a**b
        l = ds(num)
        if l>m:
            m= l

print m

