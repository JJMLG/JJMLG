import sys

n = int(input())
ls = []
dp = [0]*n
for i in range(n):
    ls.append(float(input()))


dp[0] = ls[0]
for i in range(1,n):
    if dp[i-1] * ls[i] < ls[i]:
        dp[i] = ls[i]
    else:
        dp[i] = dp[i-1]*ls[i]
print('%0.3f' % max(dp))
