import sys
sys.setrecursionlimit(99999)
sys.stdin = open('input.txt')
# from collections import deque

# 대각선 조건 몰랐음 [상, 하, 좌, 우, 좌상, 좌하, 우상, 우하]
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

# 대각선 조건 넣어야 됨
def dfs(x, y):
    visited[x][y] = 1
    stack.append([x, y])
    # print(stack)
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < h and 0 <= ny < w and land[nx][ny] == 1 and visited[nx][ny] == 0:
            land[nx][ny] = 0
            dfs(nx, ny)
            # pass

    return cnt



while True:
    w, h = map(int, input().split())
    # input 종료 조건
    cnt = 0
    if w == 0 and h == 0:
        break
    visited = [[0] * w for _ in range(h)]
    stack = []
    # print(visited)

    land = [list(map(int, input().split())) for _ in range(h)]
    # print(land)

    for i in range(len(land)):
        for j in range(len(land[i])):
            if land[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)