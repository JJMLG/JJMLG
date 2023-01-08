import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
cnt = 0
result = []

def dfs(x,y):
    global house

    arr[x][y] = -1
    house += 1
    for k in range(4):
        nx = x +dx[k]
        ny = y +dy[k]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt += 1
            house = 0
            dfs(i,j)
            result.append(house)


print(cnt)
for i in sorted(result):
    print(i)