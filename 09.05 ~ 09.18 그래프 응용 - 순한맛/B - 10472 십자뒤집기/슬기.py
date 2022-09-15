import copy
import sys
sys.stdin = open('input.txt')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
space = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

def bfs(x, y, tmp):
    if tmp[x][y] == '*':
        tmp[x][y] = '.'
    elif tmp[x][y] == '.':
        tmp[x][y] = '*'

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
            continue

        if tmp[nx][ny] == '*':
            tmp[nx][ny] = '.'
        elif tmp[nx][ny] == '.':
            tmp[nx][ny] = '*'

    return tmp


def solve(board, cnt, idx):
    global ans, arr, space

    if board == arr:
        ans = min(ans, cnt)

    if idx > 8:
        return

    x = space[idx][0]
    y = space[idx][1]

    paint_board = copy.deepcopy(board)
    paint_board = bfs(paint_board, x, y)

    solve(paint_board, cnt+1, idx+1)
    solve(board, cnt, idx+1)



p = int(input())

for _ in range(p):
    arr = [list(input() for _ in range(3))]
    init = [['.', '.', '.'] for _ in range(3)]

    ans = 1000000000

    solve(init, 0, 0)
    print(ans)