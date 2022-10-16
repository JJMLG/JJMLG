N = int(input())
arr = list(map(int, input().split()))
dp = [1] + [0] * (N-1)
for i in range(1, N):
    dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
print(max(dp))