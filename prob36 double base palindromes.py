ans =0
for k in range(1000000):
    s= str(k)
    if s==s[::-1]:
        new = bin(k)[2:]
        if new==new[::-1]:
            ans+=k

print ans
