from collections import defaultdict
nums = defaultdict(int)

sq = [i**2 for i in range(10)]

def get(n):
    temp = 0
    while n!=0:
        temp += sq[n%10]
        n/=10
    return temp

count = 0
for k in range(1, 10000000):
    new = k
    while new!=1 and new!=89:
        new = get(new)
        if nums[new] == 1:  # new will eventually lead to 89
            new = 89
    if new==89:
        count+=1
        nums[k]=1
        new = k

print count
