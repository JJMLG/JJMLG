import sys
N = int(input())
ans = [False for _ in range(1000000+1)]
ans[1]=1
ans[2]=2
x=1
# def dp(x):
#     if ans[x] != False or x < 3:
#         return ans[x]
#     ans[x] = (dp(x-1)%15746 + dp(x-2)%15746)
#     return ans[x]
while x <= N:
    if x <=2 :
        x +=1
        pass
    else:
        ans[x] = (ans[x-2] + ans[x-1])%15746
        x += 1
print(ans[N])
