import sys

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0]*(n+1)
    if n ==1:
        print(1)
        continue
    if n == 2:
        print(1)
        continue
    dp[1] = 1
    dp[2] = 1
    for i in range(3,n+1):
        dp[i] = dp[i-3] + dp[i-2]
    
    print(dp[n])

