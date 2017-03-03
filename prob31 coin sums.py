from time import time
start=time()

# A very bad bruteforce. Takes fucking 10 seconds to run.
# count = 0
# for a in range(201):
#     for b in range(101):
#         print b
#         if a+2*b>200:
#             break
#         for c in range(41):
#             if a+2*b+5*c>200:
#                 break
#             for d in range(21):
#                 if a+2*b+5*c+10*d>200:
#                     break
#                 for e in range(11):
#                     if a+2*b+5*c+10*d+20*e>200:
#                         break
#                     for f in range(5):
#                         if a+2*b+5*c+10*d+20*e+50*f>200:
#                             break
#                         for g in range(3):
#                             if a+2*b+5*c+10*d+20*e+50*f+100*g>200:
#                                 break
#                             for h in range(2):
#                                 if a+2*b+5*c+10*d+20*e+50*f+100*g+200*h == 200:
#                                     count+=1

# A fast DP approach
coins  = [1,2,5,10,20,50,100,200]
ways = [0]*201   # ways[i] will contains number of ways we can make i pences.
ways[0] = 1   # 1 way to make 0p. Don't selct any coin.

for coin in coins:
    for i in range(coin, 201):
        ways[i]+=ways[i-coin]


print "Time-",time()-start, "seconds."
print ways[200]
