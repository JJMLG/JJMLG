import sys
sys.setrecursionlimit(99999)
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    cnt = 0
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        apartment[x][y] = 0

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < T and 0 <= ny < T and apartment[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = 1
                cnt += 1

    return cnt


T = int(input())
apartment = [list(map(int, input())) for _ in range(T)]

visited = [[0] * T for _ in range(T)]
# print(visited)
# print(apartment)
house = 0
order = []

for i in range(T):
    for j in range(T):
        if apartment[i][j] == 1:
            result = bfs(i, j)
            house += 1
            order.append(result + 1)

print(house)
order.sort()

for l in order:
    print(l)