s= ''
k=1
while len(s)<1000000:
    s+= str(k)
    k+=1

ans = 1
i=1
while i<=1000000:
    ans *= int(s[i-1])
    i*=10

print ans
