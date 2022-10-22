import sys
sys.stdin = open('input.txt')
sys.stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))


cal = [0] * (n+1)

for _ in range(m):
    a, b, k = map(int, input().split())
    cal[a-1] += k
    cal[b] -= k

dp = [0] * (n+1)
dp[0] = cal[0]

for i in range(1, n+1):
    dp[i] = dp[i-1] + cal[i]

for i in range(n):
    print(h[i] + dp[i], end=' ')