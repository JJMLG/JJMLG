N = int(input())
arr = [0] + [list(map(int, input().split())) for _ in range(N)]
dp = [0, arr[1][2]] + [0]*(N-1)
if N > 1:
    for i in range(2, N+1):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i][2])
print(dp[-1])
