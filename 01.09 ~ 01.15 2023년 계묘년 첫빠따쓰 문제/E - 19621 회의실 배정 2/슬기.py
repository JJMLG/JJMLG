import sys
sys.stdin = open('input.txt')

n = int(input())
time_table = [list(map(int, input().split())) for _ in range(n)]
time_table.sort()
# print(time_table)

dp = [0] * n
dp[0] = time_table[0][2]

for i in range(1, n):
    dp[i] = max(dp[i-1], dp[i-2] + time_table[i][2])
print(dp[n-1])
print(dp)