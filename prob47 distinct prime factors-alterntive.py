from collections import deque

def count_divisors(n):
    """
    Count the prime divisors for all the numbers below n
    """
    div = [0] * n
    for i in xrange(2, n):
        if div[i] == 0:
            yield i, 1  # prime number
            for j in xrange(i, n, i):
                div[j] += 1  # add divisor to all multiples
        else:
            yield i, div[i]

N = 4  # N consecutive numbers with N divisors
prev = deque([0] * N) # hold the last N divisor counts
for number, divisors in count_divisors(10 ** 6): # started with 3, and added 0s until I found the result
    prev.popleft()
    prev.append(divisors)
    if sum(prev) == N ** 2:
        print "First number in sequence: %d" % (number - N + 1)
        break
