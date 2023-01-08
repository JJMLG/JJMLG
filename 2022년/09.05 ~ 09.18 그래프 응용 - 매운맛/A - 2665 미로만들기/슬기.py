import sys
sys.stdin = open('input.txt')
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
room = [list(map(int, input())) for _ in range(n)]


def bfs():
    q = deque()
    q.append([0, 0])
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = 0

    while q:
        x, y = q.popleft()

        if x == n-1 and y == n-1:
            return visited[x][y]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if room[nx][ny] == 1:
                    # 흰 방 먼저 탐색
                    q.appendleft([nx, ny])
                    visited[nx][ny] = visited[x][y]
                else:
                    # 검은방이면
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

print(bfs())