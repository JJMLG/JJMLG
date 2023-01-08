
import sys
from pprint import pprint
from collections import deque
sys.stdin=open('input.txt')

arr = deque(list(input()) for _ in range(8))
visited = [[0]*8 for _ in range(8)]


dx = [-1,1,0,0,0,1,1,-1,-1]
dy = [0,0,-1,1,0,-1,1,-1,1]

def bfs():
    queue = deque()
    queue.append([7,0])

    time = 0
    while queue:
        visited = [[0]*8 for _ in range(8)]
        for _ in range(len(queue)):
            x,y = queue.popleft()
            if arr[x][y] == '#':
                continue
            if x == 0 and y == 7:
                
                return 1
            
            for k in range(9):
                nx = x +dx[k]
                ny = y +dy[k]
                if 0 <= nx < 8 and 0 <= ny < 8 and arr[nx][ny] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx,ny])
                    
        arr.pop()
        arr.appendleft(['.']*8)

        time += 1
        if time == 9:
            return 1




    return 0
print(bfs())