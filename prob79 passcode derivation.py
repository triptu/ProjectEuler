count = 0

# n**10 has n+1 digits. Checking at which power this breaks for 9.
for maxPow in range(1, 50):
    if len(str(9**maxPow))!=maxPow:
        break
print maxPow

for power in range(1, maxPow):
    for num in range(1, 10):
        if len(str(num**power))==power:
            count+=1

print count
