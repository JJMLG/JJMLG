import sys

input = sys.stdin.readline

N = int(input().rstrip())
dp = [float(input().rstrip()) for _ in range(N)]
for i in range(1, N): dp[i] = max(dp[i], dp[i]*dp[i-1])
print(f'{max(dp):.3f}')