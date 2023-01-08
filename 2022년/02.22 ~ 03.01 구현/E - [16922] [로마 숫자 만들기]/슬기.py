import sys
sys.stdin = open('input.txt')

n = int(input())

dp = [0] * (n+10)

dp[0] = 0
dp[1] = 4
dp[2] = 10
dp[3] = 20
dp[4] = 35


for i in range(5, n+10):
    dp[i] = dp[i-1] - dp[i-2] + dp[i-3]
print(dp[n])