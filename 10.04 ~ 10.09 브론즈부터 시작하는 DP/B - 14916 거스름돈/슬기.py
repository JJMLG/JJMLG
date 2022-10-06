import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

dp = [-1] * (n+5)

dp[2] = 1
dp[4] = 2
dp[5] = 1
dp[6] = 3
dp[7] = 2
dp[8] = 4

for i in range(9, n+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1
print(dp[n])

