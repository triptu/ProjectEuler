def isPrime(n):
    if n==2 or n==3:
        return True
    if n<=1 or n%2==0 or n%3==0:
        return False
    if n%6!=1 and n%6!=5:   # Prime numbers > 3 are in form of 6k +/- 1.
        return False
    sqr = int(n**0.5 + 0.5)
    for i in range(5, sqr+1, 6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

def istruncprime(n):
    if not(isPrime(n)):
        return False
    n = str(n)
    for k in range(1, len(n)+1):
        new = int(n[:k])
        new2 = int(n[-k:])
        if not(isPrime(new)) or not(isPrime(new2)):
            return False
    return True

count = 0
i = 11
ans = 0
while count<11:
    if istruncprime(i):
        ans+=i
        count+=1
    i+=1

print ans
