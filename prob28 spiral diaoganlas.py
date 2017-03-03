diff = 2
curr = 1
tot = 1
for i in range(1, 500*4+1):
    curr+=diff
    tot+=curr
    if i%4==0:
        diff+=2
print tot
