import sys

N = int(input())
ans = [False] * (90+1)
ans[1] = 1
ans[2] = 1

def dp(x):
    if ans[x] != False:
        return ans[x]
    else:
        ans[x] = dp(x-2) + dp(x-1)
        return ans[x]
dp(N)
print(ans[N])
