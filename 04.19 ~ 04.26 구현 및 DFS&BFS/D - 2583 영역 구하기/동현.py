import sys
sys.setrecursionlimit(100000)


def dfs(x,y):
    global area
    arr[x][y] = 1
    area += 1
    for w in range(4):
        nx = x +dx[w]
        ny = y +dy[w]
        if 0 <= nx < m and 0 <= ny < n:
            if arr[nx][ny] == 0:

                dfs(nx,ny)

dx = [0,0,1,-1]
dy = [1,-1,0,0]
m,n,k = map(int,input().split())

arr = [[0]*n for _ in range(m)]

for i in range(k):
    a,b,c,d = map(int,input().split())

    for j in range(b,d):
        for p in range(a,c):
            arr[j][p] = 1

cnt = 0
result = []
for t in range(m):
    for q in range(n):
        if arr[t][q] == 0:
            cnt += 1
            area = 0
            dfs(t,q)
            result.append(area)

print(cnt)
print(*sorted(result))