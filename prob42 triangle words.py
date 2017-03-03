handle= open('input42.txt')
words = []

for line in handle:
    words.extend(map(lambda s: s.strip('" '), line.split(',')))

def wordValue(s):
    ans = 0
    for k in s:
        ans+= (ord(k)- ord('A')+1)
    return ans

m= 0
for word in words:
    if wordValue(word)>m:
        m = wordValue(word)

triangleNums = [1]
i = 1
while triangleNums[-1]<179:
    i+=1
    triangleNums.append((i*(i+1))/2)

count = 0
for word in words:
    if wordValue(word) in triangleNums:
        count+=1

print count
