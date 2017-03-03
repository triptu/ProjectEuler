from euler import isPrime

curr = 1
diff = 2
primecount = 0
side = 1
while (primecount/(side*2.0-1))>0.1 or primecount==0:
    for k in range(4):
        curr = curr + diff
        if isPrime(curr):
            primecount+=1
    diff+=2
    side+=2

print side
