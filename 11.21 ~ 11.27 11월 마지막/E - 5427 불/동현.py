import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    arr = [list(input()) for _ in range(n)]
    flag = 0
    visited = [[0]*m for _ in range(n)]
    visited_2 = [[0]*m for _ in range(n)]
    fire = deque()
    man = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '*':
                fire.append([i,j])
            elif arr[i][j] == '@':
                man.append([i,j])
    


    while True:
        
        for i in range(len(fire)):
            
            x,y = fire.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != '#' and visited_2[nx][ny] == 0:
                    arr[nx][ny] = '*'
                    fire.append([nx,ny])
                    visited_2[nx][ny] = 1
      
        for i in range(len(man)):
            x,y = man.popleft()

            if  x == 0 or x == n-1 or y == 0 or y == m-1:
                flag = visited[x][y] + 1
                break
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '.' and visited[nx][ny] == 0:
                    arr[nx][ny] = '@'
                    man.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
        
        
        if flag != 0:
            print(flag)
            break
        if len(man) == 0 and len(fire) == 0:
            print('IMPOSSIBLE')
            break
        