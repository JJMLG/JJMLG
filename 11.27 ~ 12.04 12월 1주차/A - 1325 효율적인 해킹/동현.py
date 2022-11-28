
import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input.txt')

n,m = map(int,input().split())
arr = [[]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
print(arr)

def dfs(hack):
    global cnt
    cnt += 1
    visited[hack] = 1
    for i in range(n+1):
        for j in range(arr[i]):
            if arr[i][j] == hack and visited[i] == 0:
                dfs(i)


visited = [0]*(n+1)

for i in arr:
    cnt = 0
    if len(arr[i]) != 0:
        dfs(i)
    print(cnt)