from collections import deque
import sys

input=sys.stdin.readline
n,m,r = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]



dx = [1,0,-1,0]
dy = [0,1,0,-1]

# w = 0
# tmp = arr[1][1]
# visited = [[0] * (m) for _ in range(n)]
def dfs(x,y,ix):
    global w,tmp,ival
    visited[x][y] = 1
    arr[x][y],tmp = tmp, arr[x][y]

    nx = x +dx[w]
    ny = y +dy[w]

    if 0+ix <= nx < n-ix and 0+ix <= ny < m-ix and visited[nx][ny] ==0:
        # arr[nx][ny] = arr[x][y]
        dfs(nx,ny,ix)
    else:

        w += 1
        if w == 4:
            if ival != tmp:
                arr[ix][ix] = tmp
            return
        nx = x + dx[w]
        ny = y + dy[w]
        # arr[nx][ny] = arr[x][y]
        dfs(nx,ny,ix)

# dfs(1,1,1)
# print(arr)
for j in range(r):
    visited = [[0] * (m) for _ in range(n)]
    for i in range(min(n,m)//2):
        tmp = arr[i][i]
        ival = arr[i][i]

        w = 0
        dfs(i,i,i)

for p in arr:
    for t in p:
        print(t, end=' ')
    print()
