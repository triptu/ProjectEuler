from time import time
start = time()

def gcd(a,b):
    if b==0:
        return a
    return gcd(b , a%b)

ansNum = 1
ansDenom = 1
for i in range(10, 100):
    for j in range(i+1, 100):
        Gcd = gcd(i,j)
        num = i/Gcd
        denom = j/Gcd
        num2, denom2 = 0, 0
        # Express i = 10*a +b and j=10*c+d
        a, b, c, d = i/10, i%10, j/10, j%10
        if b==0 and d==0:
            continue
        if a==c:
            num2, denom2 = b, d
        elif a==d:
            num2, denom2 = b, c
        elif b==c:
            num2, denom2 = a, d
        elif b==d:
            num2, denom2 = a, c
        else:
            continue
        g = gcd(num2, denom2)
        num2, denom2 = num2/g, denom2/g
        if num==num2 and denom==denom2:
            print i, j
            ansNum*=i
            ansDenom*=j
print "Time taken -", time()-start, "seconds."
print "Answer -", ansDenom/(gcd(ansDenom, ansNum))
