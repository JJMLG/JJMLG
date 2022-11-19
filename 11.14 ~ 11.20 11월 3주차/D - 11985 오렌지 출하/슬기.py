import sys
sys.stdin = open('input.txt')


n, m, k = map(int, input().split())
orange = [0]

for _ in range(n):
    orange.append(int(input()))
# print(orange)

dp = [0] * (n+1)
dp[1] = k

for i in range(2, n+1):
    a = b = orange[i]

    dp[i] = dp[i-1] + k
    for s in range(2, min(m, i)+1):
        j = i - s + 1

        a, b = min(a, orange[j]), max(b, orange[j])

        cost = k + s*(b-a)
        dp[i] = min(dp[i], dp[j-1]+cost)
print(dp[n])