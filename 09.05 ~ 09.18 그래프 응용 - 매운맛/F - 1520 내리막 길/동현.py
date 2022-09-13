import sys
from collections import deque
import copy 
from pprint import pprint
sys.stdin = open('input.txt')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
def dfs(x,y):
    global ans
    if x == n-1 and y == m-1 :
        return 1
    if visited[x][y] == -1:
        visited[x][y] = 0

        for k in range(4):
            nx = x +dx[k]
            ny = y +dy[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] < arr[x][y]:
                visited[x][y] += dfs(nx,ny)
        
    return visited[x][y]

ans = 0 
print(dfs(0,0))