import sys
sys.setrecursionlimit(15000)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,word):
    visited_1[x][y] = 1

    for k in range(4):
        nx = x +dx[k]
        ny = y +dy[k]
        if 0 <= nx < n and 0 <= ny < n and visited_1[nx][ny] == 0 and arr[nx][ny] == word:

            dfs(nx,ny,word)

def dfs_2(x,y,word):
    visited_2[x][y] = 1

    for k in range(4):
        nx = x +dx[k]
        ny = y +dy[k]
        if 0 <= nx < n and 0 <= ny < n and visited_2[nx][ny] == 0:
            if word == 'R':
                if arr[nx][ny] == 'B':
                    continue
                else:
                    dfs_2(nx,ny,arr[nx][ny])
            if word == 'G':
                if arr[nx][ny] == 'B':
                    continue
                else:
                    dfs_2(nx,ny,arr[nx][ny])
            if word == 'B':
                if arr[nx][ny] == 'B':
                    dfs_2(nx,ny,arr[nx][ny])
            

n = int(input())
arr = []
visited_1 = [[0]*n for _ in range(n)]
visited_2 = [[0]*n for _ in range(n)]
cnt_1 = 0
cnt_2 = 0
for i in range(n):
    arr.append(list(input()))


for i in range(n):
    for j in range(n):
        if visited_1[i][j] == 0:
            cnt_1 += 1
            dfs(i,j,arr[i][j])
        if visited_2[i][j] == 0:
            cnt_2 += 1
            dfs_2(i,j,arr[i][j])
print(cnt_1,cnt_2)
