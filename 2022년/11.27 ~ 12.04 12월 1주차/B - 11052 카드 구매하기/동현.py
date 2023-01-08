import sys

n = int(input())
ls = [0] + list(map(int,input().split()))
dp = [0]*(n+1)


for i in range(1,n+1):
    # if i > 0:
    #     break
    for j in range(i,n+1):
    

        dp[j] = max(dp[j],ls[i]+dp[(j-i)])
print(dp[n])


