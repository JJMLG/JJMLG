
import sys
from collections import deque   
sys.stdin = open('input.txt')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
 
    if x == n-1 and y == m-1 :
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]
    
    ways = 0
    for k in range(4):
        nx = x +dx[k]
        ny = y +dy[k]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] < arr[x][y]:
            ways += dfs(nx,ny)
    
    visited[x][y] = ways
    return visited[x][y]

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

    

