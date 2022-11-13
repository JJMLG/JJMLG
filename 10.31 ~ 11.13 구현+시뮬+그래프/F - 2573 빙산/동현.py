import sys

sys.setrecursionlimit(10**4)
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def melt(x,y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] <= 0:
            visited[x][y] += 1

def dfs(x,y):
    visited_2[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] > 0 and visited_2[nx][ny] == 0:
            dfs(nx,ny)
            

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]


time = 0
while True:
    visited = [[0]*m for _ in range(n)]
    visited_2 = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                melt(i,j)

    
    for p in range(n):
        for t in range(m):
            arr[p][t] -= visited[p][t]

    
    for z in range(n):
        for x in range(m):
            if visited_2[z][x] == 0 and arr[z][x] > 0:
                cnt += 1
                dfs(z,x)
    
    time += 1
    
    if cnt == 0:
        time = 0
        break
    
    if cnt >= 2:
        break

print(time)

