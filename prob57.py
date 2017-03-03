num = 1
denom = 2
count = 0

for k in range(1000):
    num = denom+num      # 1 + n/d = (n+d)/d
    if len(str(num))>len(str(denom)):
        count+=1
    num = denom+num     # 1 + (1+n/d) = (n+2*d)/d . One d already added to num.
    num, denom = denom, num   # 1/(1 + (1 + n/d))

print count
