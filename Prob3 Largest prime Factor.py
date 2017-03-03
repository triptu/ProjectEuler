from timeit import timeit

# Reasonably fast. 12 digit number in 0.00087 seconds.
def maxPrimeFactor(n=600851475143):
    lastFactor = 1
    if n==1:
        return 1
    elif n%2==0:
        while n%2==0:
            n/=2
        lastFactor = 2
    currFactor = 3
    maxFactor = int(n**0.5 + 0.5)  # Every number can have at most 1 prime factor greater than its root.
    while n!=1:
        if n%currFactor!=0:
            currFactor+=2
            continue
        while n%currFactor == 0:
            n/=currFactor
        if currFactor>=maxFactor:
            return currFactor
        lastFactor = currFactor
        currFactor+=2
        maxFactor = int(n**0.5+0.5)
    return lastFactor

print maxPrimeFactor()
# t = timeit(maxPrimeFactor, number = 1000)
# print t/1000
