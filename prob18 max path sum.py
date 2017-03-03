nums=[]
handle = open('input18.txt')
for k in handle:
    new = map(int, k.strip().split())
    nums.append(new)

dp = []
for k in range(100):
    temp = [-1 for i in range(k+1)]
    dp.append(temp)

def solve(pos, level):
    if level==99:
        return nums[level][pos]
    if dp[level][pos]!=-1:
        return dp[level][pos]
    dp[level][pos] = nums[level][pos] + max(solve(pos, level+1), solve(pos+1, level+1))
    return dp[level][pos]
print solve(0, 0)

