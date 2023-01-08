N = int(input())
cards = list(map(int, input().split()))
dp = [0]*(N+1)
for i in range(1, N+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[j]+cards[i-j-1])
print(dp[-1])

"""
dp[i] = max(
    dp[1] + cards[i-1],
    dp[2] + cards[i-2],
    ...
    dp[i-2] + cards[2],
    dp[i-1] + cards[1],
)
"""