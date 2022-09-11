import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, arr):
    global cnt, visited
    final_board = [[0] * 3 for _ in range(3)]
    q = deque()
    q.append(final_board)
    visited[x][y] = 1
    # print(q)
    while q:
        l = len(q)

        for _ in range(l):
            board = q.popleft()
            if board == final_board:
                return cnt

    # if visited[x][y] == 1:
    #     visited[x][y] = 0
    #
    # for z in range(4):
    #     nx = x + dx[z]
    #     ny = y + dy[z]
    #
    #     if 0 <= nx < 3 and 0 <= ny < 3 and visited[nx][ny] == 1:
    #         visited[nx][ny] = 0
    #         bfs(nx, ny)
    #         print(visited)


p = int(input())

for _ in range(p):
    board = list(input() for _ in range(3))
    # print(board)
    change_board = [[0] * 3 for _ in range(3)]
    visited = [[0] * 3 for _ in range(3)]
    # print(visited)
    cnt = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == '*':
                change_board[i][j] = 1

    for i in range(3):
        for j in range(3):
            if change_board[i][j] == 1:
                # visited[i][j] = 0
                bfs(i, j, change_board)
    print(cnt)