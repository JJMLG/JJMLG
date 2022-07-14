import sys
from collections import deque

arr = deque(list(input()) for _ in range(8))

dx = [-1,1,0,0,0,-1,1,-1,1]
dy = [0,0,-1,1,0,-1,1,1,-1]


queue = deque()
queue.append((7,0))
result = 0
time = 0
while queue:
   
    visited = [[0]*8 for _ in range(8)]
    for i in range(len(queue)):
        x, y = queue.popleft()
        if arr[x][y] == '#':
            continue
        if x == 0 and y == 7:
            result = 1
            break

        for k in range(9):
            nx = x +dx[k]
            ny = y +dy[k]
            if 0 <= nx < 8 and 0 <= ny < 8:
                if arr[nx][ny] == '#' or visited[nx][ny] == 1:
                    continue
                visited[nx][ny] = 1
                queue.append((nx,ny))
    arr.pop()
    arr.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])
    time += 1
    if time == 9:
        result = 1
        break

print(result)