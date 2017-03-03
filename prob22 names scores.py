handle = open("input22.txt")
names=[]
for line in handle:
    words = map(lambda s: s.strip('" '), line.split(','))
    names.extend(words)

def calc(s):
    tot = 0
    for k in s:
        tot+=(ord(k)- ord('A')+1)
    return tot
names.sort()
ans = 0
for pos, name in enumerate(names):
    ans+=(calc(name)*(pos+1))
print ans


