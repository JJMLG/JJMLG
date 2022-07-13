import sys
from collections import deque
sys.stdin=open('input.txt')
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]


queue = deque()
queue.append([0,0,0])    
cnt = 0
visited[0][0][0] = 1
while queue:
    x,y,z = queue.popleft()

    if x== n-1 and y == m-1:
        print(visited[x][y][z])
        cnt = 1
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] +1
                queue.append([nx,ny,1])
            elif arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append([nx,ny,z])
   
if not cnt:
    print(-1)
