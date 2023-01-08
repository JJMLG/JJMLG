import sys

from collections import deque
from pprint import pprint


n,m = map(int,input().split())
arr = [[]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[b].append(a)


def dfs(start):
    global cnt
    
    # for i in range(len(arr[start])):
    #     if visited[arr[start][i]] == 0:
    #         cnt += 1
    #         visited[arr[start][i]] = 1
    #         dfs(arr[start][i])
    queue = deque()
    queue.append(start)

    while queue:
        t = queue.popleft()
        for i in range(len(arr[t])):
            if visited[arr[t][i]] == 0:
                cnt += 1
                visited[arr[t][i]] = 1
                queue.append(arr[t][i])
            

visited = [0]*(n+1)
cnt = 0
maxx = 0
nums = []
for i in range(len(arr)):
    if arr[i]:
        visited[i] = 1
        cnt += 1
        dfs(i)
        
        if cnt > maxx:
            maxx = cnt
            nums = [i]
        elif cnt == maxx:
            nums.append(i)

        visited = [0]*(n+1)
        cnt = 0

print(*nums)
    

    
