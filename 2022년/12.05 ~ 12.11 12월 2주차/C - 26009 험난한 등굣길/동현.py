
import sys


from collections import deque
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int,input().split())
k = int(input())
arr = [[0]*(m+1) for _ in range(n+1)]
visited = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
    r,c,d = map(int,input().split())

    for i in range(0,d):
        if r - d + i >= 1:
           
            if c - i >= 1:
                visited[r - d + i][c - i] = 1
            if c + i <= m:
                visited[r - d + i][c + i] = 1
          
        if r + d - i <= n:
            if c - i >= 1:
                visited[r + d - i][c - i] = 1
            if c + i <= m:
                visited[r + d - i][c + i] = 1
    if c - d >= 1:
            visited[r][c - d] = 1
    if c + d <= m:
        visited[r][c + d] = 1


def bfs():
    queue = deque()
    queue.append((1,1))
    visited[1][1] = 1

    while queue:
       
        x,y = queue.popleft()
        
        if x == n and y == m:
            print('YES')
            print(visited[x][y]-1)
            return
        for k in range(4):
            nx = x +dx[k]
            ny = y +dy[k]
            if 0 < nx < n+1 and 0 < ny < m+1 and visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1

    print('NO')
bfs()      
    
    
        

