from time import time
start = time()

fact= [1]
prod=1
for k in range(1,10):
    prod*=k
    fact.append(prod)
ans=0

for a in range(3,41000):
    digits = map(int, str(a))
    temp = 0
    for k in digits:
        temp+=fact[k]
    if temp==a:
        ans+=a
        curr=a
print ans
print time()-start, "seconds"
