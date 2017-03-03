tot=0
# 354295 comes by experimenting. Even if all the digits will be 9, sum will reach 9**5*6 = 3549294
for k in range(2,354295):
    if sum(map(lambda x: int(x)**5, str(k)))==k:
        tot+=k
print tot
