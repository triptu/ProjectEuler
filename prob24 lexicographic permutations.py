fact=[1]
prod=1
for k in range(1, 10):
    prod*=k
    fact.append(prod)

count = 0
nums = list('0123456789')
ans = ''
kf = 9
while count<1000000 and kf>=0:
    pos=0
    while count+fact[kf]<1000000:
        count+=fact[kf]
        pos+=1
    kf-=1
    ans+=nums.pop(pos)
print ans
