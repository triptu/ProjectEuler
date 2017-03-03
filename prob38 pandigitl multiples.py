ans = 0
for i in range(2, 9999):
    n = str(i)
    k = 2
    while len(n)<9:
        n += str(i*k)
        k+=1
    if len(n)!=9:
        continue
    nums = [0]*10
    for k in n:
        nums[int(k)]=1
    if nums[1:]==[1]*9:
        if int(n)>ans:
            ans = int(n)

print ans
