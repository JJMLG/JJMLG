import sys

n,m = map(int,input().split())
ls = list(map(int,input().split()))
summ = [0]*(n+1)
result = [0]*(n+1)
ans = []
for i in range(m):
    a,b,k = map(int,input().split())
    summ[a-1] +=k
    summ[b] -=k
result[0] = summ[0]
for j in range(1,n+1):
    result[j] = result[j-1] + summ[j]

for k in range(n):
    ans.append(result[k]+ls[k])

print(*ans)