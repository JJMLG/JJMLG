import sys
from pprint import pprint
from collections import deque
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global visited, cnt
    q = deque()
    q.append([x, y])
    # local[x][y] += 1
    # print(x,y)
    # visited[x][y] += 1
    while q:
        # print(q)
        f, s = q.popleft()

        # print(f, s, '?')
        for l in range(4):
            nnx = f + dx[l]
            nny = s + dy[l]

            if nnx == n and nny == m:
                # cnt += 1
                return cnt

            if 0 <= nnx <= n and 0 <= nny <= m and local[nnx][nny] == 0:
                visited[nnx][nny] = visited[f][s] + 1
                local[nnx][nny] = 1
                cnt += 1
                bfs(nnx, nny)
                pprint(local)
                pprint(visited)

    return cnt

n, m = map(int, input().split())
k = int(input())

local = [[0] * (m+1) for _ in range(n+1)]
# pprint(local)
local[1][1] = 3 # 내위치
local[n][m] = 2 # 학교
visited = [[0] * (m+1) for _ in range(n+1)]
# print(visited)
for _ in range(k):
    r, c, d = map(int, input().split())
    local[r][c] = 1
    # print(local)
    for _ in range(d):
        for k in range(4):
            nx = r + dx[k]
            ny = c + dy[k]
            # print(nx, ny)
            if 0 <= nx <= n and 0 <= ny <= m and local[nx][ny] == 0:
                local[nx][ny] = 1
                # print(nx, ny)
pprint(local)
res = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if local[i][j] == 3:
            res = bfs(i, j)
print(res)