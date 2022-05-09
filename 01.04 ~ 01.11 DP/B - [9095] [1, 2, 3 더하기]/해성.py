import sys
# sys.setrecursionlimit(10**6)

dp =[False for _ in range(12)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
# print(dp)
def dpmaker(x):
    if dp[x] != False:
        return dp[x]
    elif dp[x] == False:
        dp[x] = dpmaker(x-1) + dpmaker(x-2) + dpmaker(x-3)
    return dp[x]

N = int(input())
for _ in range(N):
    i = int(input())
    dpmaker(i)
    # print(dpmaker(i))
    print(dp[i])