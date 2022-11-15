import sys


n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
print(schedule)
dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i + schedule[i][0], n+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]
    print(dp)
print(dp[-1])
