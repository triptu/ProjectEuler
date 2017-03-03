pnums = {}
pnumsl = []
for n in range(1,10001):
    pnums[((n*(3*n-1))/2)]=1
    pnumsl.append(((n*(3*n-1))/2))

for a in range(10000):
    for b in range(a+1, 10000):
        if (pnumsl[a]+pnumsl[b]) in pnums and (pnumsl[b]-pnumsl[a]) in pnums:
            # print pnumsl[a], pnumsl[b]
            print pnumsl[b]-pnumsl[a]
