import sys
sys.stdin = open('input.txt')
from collections import deque
from pprint import pprint


dx = [0, -1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, 0, -1, 1, 1, 1, -1, -1]

def bfs():
    q = deque([(7, 0)])
    chane = 0

    while q:
        visited = [[0] * 8 for _ in range(8)]

        for _ in range(len(q)):
            x, y = q.popleft()

            if maze[x][y] == '#':
                continue

            if (x, y) == (0, 7):
                return 1

            for k in range(9):
                nx = x + dx[k]
                ny = y + dy[k]

                if not (0 <= nx < 8 and 0 <= ny < 8):
                    continue

                if maze[nx][ny] == '#' or visited[nx][ny] == 1:
                    continue
                visited[nx][ny] = 1
                q.append([nx, ny])

        maze.pop()
        maze.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])

        chane += 1

        if chane == 9:
            return 1

    return 0


maze = deque(list(input() for _ in range(8)))
# pprint(maze)
print(bfs())

"""
append > '........'
pop 한줄씩
"""