import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

def bfs(a, b):
    while q:
        x, y = q.popleft()
        # 도착지점까지 'S'로 바꾸고 도착했다면, 종료조건
        if land[a][b] == 'S':
            return visited[a][b]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < r and 0 <= ny < c:
                # 고슴도치는 '.' 이나 비버 위치로만 이동 가능 > 고슴도치 이동
                if (land[nx][ny] == '.' or land[nx][ny] == 'D') and land[x][y] == 'S':
                    land[nx][ny] = 'S'
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])

                # 물은 '.', 고슴도치 위치만 이동 가능 > 물로 바꿔 주기
                elif (land[nx][ny] == '.' or land[nx][ny] == 'S') and land[x][y] == '*':
                    land[nx][ny] = '*'
                    q.append([nx, ny])

    return 'KAKTUS'


r, c = map(int, input().split())
land = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]


for i in range(r):
    for j in range(c):
        # 시작지점 입력
        if land[i][j] == 'S':
            q.append([i, j])
        # 도착지점 입력
        elif land[i][j] == 'D':
            a, b = i, j

for i in range(r):
    for j in range(c):
        # 물 위치 입력
        if land[i][j] == '*':
            q.append([i, j])

print(bfs(a, b))

"""
물이 차있는 지역은 '*'
돌은 'X'
비버의 굴은 'D'
고슴도치의 위치는 'S'
"""