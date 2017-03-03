currt = 286
currp = 165
currh = 143
flag=1
while flag==1:
    t=(currt*(currt+1))/2
    while flag==1:
        p = (currp*(currp*3 - 1))/2
        if p>t:
            break
        if t!=p:
            currp+=1
            continue
        while flag==1:
            h = currh*(currh*2 - 1)
            if h>p:
                break
            if h!=p:
                currh+=1
                continue
            print t
            flag = 0
        currp+=1
    currt+=1

