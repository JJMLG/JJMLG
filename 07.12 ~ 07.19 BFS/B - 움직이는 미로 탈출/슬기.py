import sys
sys.stdin = open('input.txt')
from collections import deque

# 제자리, 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
dx = [0, -1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, 0, -1, 1, -1, -1, 1, 1]

def bfs():
    # 처음 위치
    q = deque([(7, 0)])
    wall_change = 0

    while q:
        visited = [[0] * 8 for _ in range(8)]
        for _ in range(len(q)):
            x, y = q.popleft()
            # 시작 위치가 벽이면
            if maze[x][y] == '#':
                continue
            # 도착 위치면
            if (x, y) == (0, 7):
                return 1

            for k in range(9):
                nx = x + dx[k]
                ny = y + dy[k]

                # 범위 벗어나면
                if not (0 <= nx < 8 and 0 <= ny < 8):
                    continue

                # 벽이거나 이미 방문했으면
                if maze[nx][ny] == "#" or visited[nx][ny] == 1:
                    continue

                # 방문 체크
                visited[nx][ny] = 1
                q.append((nx, ny))

        # 벽 이동
        maze.pop()
        maze.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])

        wall_change += 1

        # 8번 다 변하고 9초 후 존재하는 벽 없으므로 탈출 가능
        if wall_change == 9:
            return 1
    # 탈출 못 하면
    return 0


maze = deque(list(input()) for _ in range(8))
print(bfs())



"""
내 주위 어느 범위 내에 #이 있으면 못 감
(7,0)에서 시작 > (0,7) 도착
"""