import sys
sys.stdin=open('input.txt')
from collections import deque

r,c = map(int,input().split())
arr = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]


biber = deque()
water = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
target = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':
            water.append((i,j))
            visited[i][j] = 1
        elif arr[i][j] == 'S':
            biber.append((i,j))
            visited[i][j] = 1
   


while biber:

    for i in range(len(water)):
        x,y = water.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.':
                water.append((nx,ny))
                arr[nx][ny] = '*'
                visited[nx][ny] = 1

    cnt += 1
    for j in range(len(biber)):
        x,y = biber.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c :
                if visited[nx][ny] == 0 and arr[nx][ny] == '.':
                    biber.append((nx,ny))
                    visited[nx][ny] = 1
                elif arr[nx][ny] == 'D':
                    print(cnt)
                    exit()

print('KAKTUS')
                    