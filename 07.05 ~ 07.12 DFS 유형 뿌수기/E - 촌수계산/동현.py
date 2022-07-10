import sys

n = int(input())
start, end = map(int,input().split())
m = int(input())
arr = [[]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
result = -1
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(find,cnt):
    global result
    if find == end:
        result = cnt
        return
    for i in arr[find]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i,cnt+1)


dfs(start,0)

print(result)