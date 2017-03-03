ans = 0
for k in range(10000):
    temp = str(k)
    count = 0
    while count<=51:
        temp = str(int(temp) + int(temp[::-1]))
        count+=1
        if temp==temp[::-1]:
            break
    if count == 52:
        ans+=1

print ans
