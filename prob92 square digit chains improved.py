# Max sum for seven digit number = 9**2*7 = 81*7 = 567.
# Intially mark all numbers till 567 which will have 89 in cycle.

cache = [0 for i in range(568)]
for k in range(1, 568):
    new = k
    while new!=1 and new!=89:
        new = sum(i**2 for i in map(int, list(str(new))))
    if new==89:
        cache[k]=1

count = 0
# The trick:- Don't calculate sum of squares which is already calculated.
for a in range(10):
    curr1= a**2
    for b in range(10):
        curr2=curr1+b**2
        for c in range(10):
            curr3=curr2+c**2
            for d in range(10):
                curr4=curr3+d**2
                for e in range(10):
                    curr5=curr4+e**2
                    for f in range(10):
                        curr6=curr5+f**2
                        for g in range(10):
                            curr7=curr6+g**2
                            if cache[curr7]==1:
                                count+=1
print count
