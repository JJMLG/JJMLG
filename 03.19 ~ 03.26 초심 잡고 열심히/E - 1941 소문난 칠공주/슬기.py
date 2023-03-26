import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[1] * 5 for _ in range(5)]

    for i in arr:
        visited[i[0]][i[1]] = 0

    q = deque([(arr[0])])
    visited[arr[0][0]][arr[0][1]] = 1
    check = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                check += 1
                q.append([nx, ny])

    if check != 7:
        return False
    else:
        return True

def dfs(depth, s, cnt):
    global res

    if cnt >= 4:
        return

    if depth == 7:
        if bfs(arr):
            res += 1
        return

    for i in range(s, 25):
        r = i // 5
        c = i % 5
        arr.append([r, c])
        dfs(depth+1, i+1, cnt + (student[r][c] == 'Y'))
        arr.pop()

student = [list(input()) for _ in range(5)]
arr = []
res = 0
dfs(0, 0, 0)
print(res)