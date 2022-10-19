import sys
sys.stdin = open('input.txt')

t = int(input())

for _ in range(t):
    n = int(input())

    dp = [0] * (n+5)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2

    for i in range(6, n+5):
        dp[i] = dp[i-3] + dp[i-2]

    print(dp[n])