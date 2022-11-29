
import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
from pprint import pprint
sys.stdin = open('input.txt')

n,m = map(int,input().split())
arr = [[]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[b].append(a)


def dfs(start):
    global cnt
    
    for i in range(len(arr[start])):
        if visited[arr[start][i]] == 0:
            cnt += 1
            visited[arr[start][i]] = 1
            dfs(arr[start][i])
            

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
    