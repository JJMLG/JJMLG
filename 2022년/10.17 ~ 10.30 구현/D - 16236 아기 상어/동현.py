import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]



def search(x,y):
    global ans
    global pos

    dist = 987654321
    for i in range(n):
        for j in range(n):
            if arr[i][j] < shark and arr[i][j] != 0:

                visited = [[0]*n for _ in range(n)]
                tmp = bfs(x,y,visited,i,j)
                if not tmp:
                    continue
                if tmp < dist:
                    dist = tmp
                    pos = [i,j]
    arr[pos[0]][pos[1]] = 0
    if dist == 987654321:
        return -1
    else:
        return dist
    
                
def bfs(sx,sy,visited,i,j):
    queue = deque()
    queue.append([sx,sy])

    visited[sx][sy] = 1

    while queue:
        x,y = queue.popleft()
        if x== i and y == j:

            return visited[x][y] -1
        for k in range(4):
            nx = x +dx[k]
            ny = y +dy[k]
      
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] <= shark:
                
                queue.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
shark = 2
for i in range(n):
    for j in range(n):
        
        if arr[i][j] == 9:
            pos = [i,j]
            arr[i][j] = 0
ans = 0
feed = 0 
while True:

    time = search(pos[0],pos[1])
    feed += 1
    if feed == shark:
        shark += 1
        feed = 0
    if time == -1:
        print(ans)
        break
    else:
        ans += time
