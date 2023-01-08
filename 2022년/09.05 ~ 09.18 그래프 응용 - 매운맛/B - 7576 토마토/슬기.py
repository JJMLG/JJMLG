import sys
sys.stdin = open('input.txt')
from collections import deque

m, n = map(int, input().split())
ground = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([])

for i in range(n):
    ground.append(list(map(int, input().split())))

    for j in range(m):
        if ground[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and ground[nx][ny] == 0:
                q.append([nx, ny])
                ground[nx][ny] = ground[x][y] + 1

bfs()
cnt = 0

for i in ground:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
print(cnt-1)