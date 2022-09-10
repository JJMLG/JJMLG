import sys
from collections import deque



n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            queue.append([i,j])
            visited[i][j] = 1

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0 and visited[nx][ny] == 0:
            queue.append([nx,ny])
            visited[nx][ny] = visited[x][y] + 1

maxx = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and visited[i][j] == 0:
            print(-1)
            exit()
        if visited[i][j] > maxx:
            maxx = visited[i][j]

print(maxx-1)
