import sys
sys.stdin = open('input.txt')

m, n = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
# print(visited)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# chain = [[0, 0], [0, 1], []]

def bfs(x, y):
    pass


for i in range(n):
    for j in range(m):
        if ground[i][j] == 1:
            bfs(i, j)