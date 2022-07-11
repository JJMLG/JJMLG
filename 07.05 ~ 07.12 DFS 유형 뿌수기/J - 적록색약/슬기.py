import sys
sys.setrecursionlimit(9999)
input = sys.stdin.readline


nomal = 0
weak = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = 1
    current_color = color[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0:
                if color[nx][ny] == current_color:
                    dfs(nx, ny)



n = int(input())

color = [list(input().rstrip()) for _ in range(n)]
# print(color)
visited = [[0] * n  for _ in range(n)]
# print(visited)

for l in range(n):
    for m in range(n):
        if visited[l][m] == 0:
            dfs(l, m)
            nomal += 1

# 적록색약일 경우 색깔 같게 맞춰주기
for i in range(n):
    for j in range(n):
        if color[i][j] == 'R':
            color[i][j] = 'G'

visited = [[0] * n for _ in range(n)]

for a in range(n):
    for b in range(n):
        if visited[a][b] == 0:
            dfs(a, b)
            weak += 1

print(nomal, weak)
