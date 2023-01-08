import sys

def dfs(start):

    for k in arr[start]:
        if visited[k] == 0:
            visited[k] = 1
            dfs(k)

t = int(input())
for tc in range(t):
    n = int(input())
    ls = list(map(int,input().split()))
    visited = [0]*(n+1)
    cnt = 0
    arr = [[]*(n+1) for _ in range(n+1)]
    for i in range(n):
        arr[i+1].append(ls[i])
    
    for j in range(1,n+1):
        if visited[j] == 0:
            cnt += 1
            dfs(j)
    
    print(cnt)