"""
dp[n] = p[n]
        dp[n-1] + p[1]
        dp[n-2] + p[2]
        ...
        dp[1] + p[n-1]
        중에서 최대값
"""

N = int(input())
P = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[1] = P[1]

for i in range(2, N + 1):
    p = P[i]
    for j in range(1, i):
        p = max(p, dp[i - j] + P[j])
    dp[i] = p

print(dp[N])
