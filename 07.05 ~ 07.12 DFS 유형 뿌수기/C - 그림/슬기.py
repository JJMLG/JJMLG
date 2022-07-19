import sys
sys.setrecursionlimit(99999)
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    total = 1
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if paper[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    total += 1

    return total

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

cnt = 0
big = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            big = max(big, bfs(i, j))

print(cnt)
print(big)