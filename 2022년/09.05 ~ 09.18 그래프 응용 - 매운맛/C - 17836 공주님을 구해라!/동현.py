import sys
from collections import deque


n, m, t  = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 10001
def bfs():
    global ans
    queue = deque()
    queue.append([0,0])
    visited[0][0] = 0
    while queue:
        x,y = queue.popleft()
        if x == n-1 and y == m-1:
            return min(ans,visited[x][y])
            
        if arr[x][y] == 2:
            ans = n-x +m-y + visited[x][y] -2
            
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and arr[nx][ny] != 1:
                queue.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1
    
    return ans


answer = bfs()
if answer <=t :
    print(answer)
else:
    print("Fail")
