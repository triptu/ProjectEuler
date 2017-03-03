''' Possible only if one number is 2 digits and other 3 digits or
 one is 1 digit and the other 4 digits.
 '''
count = 0
ans = 0
prods=[]
for i in range(10,100):
    for j in range(100, 1000):
        prod = str(i)+str(j)+str(i*j)
        if len(prod)>9:
            break
        nums= [0]*10
        for k in prod:
            nums[int(k)]+=1
        if nums[1:] == [1]*9:
            if (i*j) not in prods:
                count+=1
                print i, j, i*j
                prods.append(i*j)
                ans+= i*j

for i in range(1, 10):
    for j in range(1000, 10000):
        prod = str(i)+str(j)+str(i*j)
        if len(prod)>9:
            break
        nums= [0]*10
        for k in prod:
            nums[int(k)]+=1
        if nums[1:] == [1]*9:
            if (i*j) not in prods:
                count+=1
                print i, j, i*j
                prods.append(i*j)
                ans+= i*j

print count
print "Answer - ", ans
