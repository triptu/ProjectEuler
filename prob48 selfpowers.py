tot=0
for k in range(1,1001):
    tot+= k**k
new = (str(tot))[-1:-11:-1]
print new[::-1]
