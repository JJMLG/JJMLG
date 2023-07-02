def solution(n):
    dp = [0] * (n + 5)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(4, n + 5):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

    return dp[n]