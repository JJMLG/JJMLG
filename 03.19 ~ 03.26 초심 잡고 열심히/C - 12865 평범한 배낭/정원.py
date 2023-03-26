N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0]*(K+1)
for item in items:
    weight, value = item
    for i in range(K, weight-1, -1): # top-down
        dp[i] = max(dp[i], dp[i-weight]+value)
print(dp[-1])