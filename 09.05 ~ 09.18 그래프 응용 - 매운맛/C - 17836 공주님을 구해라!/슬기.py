import sys
sys.stdin = open('input.txt')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global sword
    q = []
    visited[0][0] = 1
    q.append([0, 0])

    while len(q) > 0:
        x, y = q.pop(0)
        if castle[x][y] == 2:
            sword = n-1-x + m-1-y + visited[x][y]-1

        if x == n-1 and y == m-1:
            return min(visited[x][y]-1, sword)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and castle[nx][ny] != 1:
                if visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

    return sword



n, m, t = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
sword = 1000000
res = bfs()

if res > t:
    print('Fail')
else:
    print(res)