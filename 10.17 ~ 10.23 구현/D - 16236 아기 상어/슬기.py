import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

time = 0
baby_shark = 2


def bfs(x, y):
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    eat = []
    dist = [[0] * n for _ in range(n)]
    q = deque()
    q.append([x, y])

    while q:
        t, u = q.popleft()

        for k in range(4):
            nx = t + dx[k]
            ny = u + dy[k]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if sea[nx][ny] <= sea[x][y] or sea[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[t][u] + 1

                if sea[nx][ny] < sea[x][y] and sea[nx][ny] != 0:
                    eat.append([nx, ny, dist[nx][ny]])

    if not eat:
        return -1, -1, -1
    eat.sort(key = lambda x : (x[2], x[0], x[1]))
    return eat[0][0], eat[0][1], eat[0][2]


sea = []
for i in range(n):
    arr = list(map(int, input().split()))
    sea.append(arr)
    for j in range(n):
        if arr[j] == 9:
            sea[i][j] = 2
            start = [i, j]

exp = 0
cnt = 0

while True:
    i, j = start[0], start[1]
    nx, ny, dist = bfs(i, j)

    if nx == -1:
        break

    sea[nx][ny] = sea[i][j]
    sea[i][j] = 0
    start = [nx, ny]
    exp += 1

    if exp == sea[nx][ny]:
        exp = 0
        sea[nx][ny] += 1
    cnt += dist

print(cnt)
