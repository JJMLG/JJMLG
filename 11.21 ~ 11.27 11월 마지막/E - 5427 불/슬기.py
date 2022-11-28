import sys
from pprint import pprint
from collections import deque
sys.stdin = open('input.txt')

dx = [-1, -1, 0, 0]
dy = [0, 0, -1, 1]


def fire_bfs(x, y):
    fq = deque()
    fq.append([x, y])
    visited[x][y] = 2

    while fq:
        a, b = fq.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]

            if 0 <= nx < w and 0 <= ny < h and visited[nx][ny] == 0:
                # time += 1
                visited[nx][ny] = 2
                fq.append([nx, ny])
                # print(time)
    # pprint(visited)

def bfs(x, y):
    global time
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        a, b = q.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]

            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0:
                time += 1
                visited[nx][ny] = 1
                q.append([nx, ny])
                # print(time)


t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    building = [input() for _ in range(h)]
    # pprint(building)
    visited = [[0] * w for _ in range(h)]
    # print(visited)
    time = 1
    for i in range(h):
        for j in range(w):
            # print(i, j)
            if building[i][j] == '#':
                visited[i][j] = 1
            if building[i][j] == '@':
                bfs(i, j)
            if building[i][j] == '*':
                visited[i][j] = 2
                # fire_bfs(i, j)

    print(visited)
    print(time)