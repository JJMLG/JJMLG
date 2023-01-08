import sys
sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def fire_bfs():
    # while fq:
    for _ in range(len(fq)):
        a, b = fq.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]

            if 0 <= nx < h and 0 <= ny < w:
                if building[nx][ny] != '#' and building[nx][ny] != '*':
                    building[nx][ny] = '*'
                    fq.append([nx, ny])

def bfs():
    go = 0

    # while q:
    for _ in range(len(q)):
        a, b = q.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]

            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == 0 and building[nx][ny] != '#' and building[nx][ny] != '*':
                    go = 1
                    visited[nx][ny] = visited[a][b] + 1
                    q.append([nx, ny])
            else:
                return visited[a][b]

    if not go:
        return 'IMPOSSIBLE'


t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    building = []
    fq = deque()
    q = deque()
    for i in range(h):
        building.append(list(input().strip()))
        # print(building)
        for j in range(w):
            if building[i][j] == '*':
                fq.append([i, j])
            if building[i][j] == '@':
                q.append([i, j])
    visited = [[0] * w for _ in range(h)]
    visited[q[0][0]][q[0][1]] = 1

    # print(visited)
    res = 0
    while True:
        fire_bfs()
        res = bfs()
        if res:
            break
    print(res)