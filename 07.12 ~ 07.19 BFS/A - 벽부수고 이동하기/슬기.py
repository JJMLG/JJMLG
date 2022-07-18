import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0, 0, 0])      # 시작이 1,1 인데 인덱스 맞추려고 0,0 함

    while q:
        x, y, z = q.popleft()

        # 도착
        if x == n-1 and y == m-1:
            return visited[x][y][z]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위 내에 있을 때
            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 만나고, 안 부술 경우 > +1 인 부분이 cnt += 1 같은 역할
                if load[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append([nx, ny, 1])

                # 벽 아니고, 방문 안 했다면 > +1 인 부분이 cnt += 1 같은 역할
                elif load[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append([nx, ny, z])

    return -1


n, m = map(int, input().split())
load = [list(map(int, input())) for _ in range(n)]

# 3차원 행렬로 벽 부수는 거 판단, visited[x][y][0] > 부수기 가능, [1]은 불가능
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

print(bfs())
