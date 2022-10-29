import sys
sys.stdin = open('input.txt')
from collections import deque


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
x, y, baby_shark = 0, 0, 2


for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            x = i
            y = j


def bfs(x, y, shark_size):
    dist = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    tmp = []

    while q:
        a, b = q.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if arr[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[a][b] + 1
                    if arr[nx][ny] < shark_size and arr[nx][ny] != 0:
                        tmp.append((nx, ny, dist[nx][ny]))

    return sorted(tmp, key=lambda x: (-x[2], -x[0], -x[1]))


cnt = 0
result = 0

while True:
    shark = bfs(x, y, baby_shark)

    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()

    result += dist
    arr[x][y], arr[nx][ny] = 0, 0

    x, y = nx, ny
    cnt += 1
    if cnt == baby_shark:
        baby_shark += 1
        cnt = 0

print(result)