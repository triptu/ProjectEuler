a =1
b=1
c= 2
ind = 1
while len(str(c))<1000:
    ind+=1
    a,b = b,c
    c=a+b
print ind+2
