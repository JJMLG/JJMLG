import sys
from pprint import pprint
from collections import deque
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

dx2 = [1, -1, 0, 0, 1, 1, -1, -1]
dy2 = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y):
    global visited, flag, cnt
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        # print(t)
        for _ in range(len(q)):
            t = q.popleft()
            f = t[0]
            s = t[1]

            for l in range(4):
                nnx = f + dx[l]
                nny = s + dy[l]

                if nnx == n and nny == m:
                    # cnt += 1
                    flag = 1
                    # return cnt + 1
                    return visited[f][s]

                if 0 < nnx <= n and 0 < nny <= m and local[nnx][nny] == 0 and visited[nnx][nny] == 0:
                    # local[nnx][nny] = 1
                    visited[nnx][nny] = visited[f][s] + 1
                    q.append([nnx, nny])

        cnt += 1

    # return cnt

n, m = map(int, input().split())
k = int(input())

local = [[0] * (m+1) for _ in range(n+1)]
# pprint(local)
local[1][1] = 3 # 내위치
local[n][m] = 2 # 학교
visited = [[0] * (m+1) for _ in range(n+1)]
# print(visited)
flag = 0
for _ in range(k):
    r, c, d = map(int, input().split())
    local[r][c] = 1
    # print(local)
    for i in range(1, d+1):
        for k in range(8):
            nx = r + dx2[k] * i
            ny = c + dy2[k] * i
            # print(nx, ny)
            if 0 <= nx <= n and 0 <= ny <= m \
                    and local[nx][ny] == 0 \
                    and abs(r-nx) + abs(c-ny) <= d:
                local[nx][ny] = 1
                # print(nx, ny)
# pprint(local)
res = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if local[i][j] == 3:
            res = bfs(i, j)

if flag == 0:
    print('NO')
else:
    print('YES')
    print(res)