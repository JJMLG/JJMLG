import sys

n = int(input())
ls = [0] + list(map(int,input().split()))
dp = [0]*(n+1)


for i in range(1,n+1):
    maxx = 0
    for j in range(i):
        if ls[i] > ls[j]:
            if dp[j] >= maxx:
                maxx = dp[j]
    
    dp[i] = maxx + 1
    
print(max(dp))