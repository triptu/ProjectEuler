from time import time
start = time()

# n needs to be multiple of 3 as n and 3*n both have same digits
n = 3

# For checking if both have same digits. Make a list of digits. Sort it. Check if they are equal.

while True:
    temp = str(n)
    digits = list(temp)
    digits.sort()
    if '0' not in digits and '5' not in digits:   # As 5*n has same digits
        n+=3
        continue
    for k in range(2,7):
        digits2 = list(str(n*k))
        digits2.sort()
        if digits!=digits2:
            break
    else:
        print n
        break

    n+=3

print "Time -", time()-start, "seconds."
