from collections import deque
import sys

from itertools import combinations
from pprint import pprint

ax,ay = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(ay)]

queue = deque()


dx1 = [-1,-1,0,0,1,1]
dy1 = [0,1,-1,1,0,1]

dx2 = [-1,-1,0,0,1,1]
dy2 = [-1,0,-1,1,-1,0]

def search():
    
    
    for i in range(ay):
        for j in range(ax):
            if arr[i][j] ==0:
              
                visited = [[0]*ax for _ in range(ay)]
                tmp = []
                queue = deque()
                queue.append((i,j))
                visited[i][j] = 1
                while queue:
                
                    x,y = queue.popleft()
                    if x == 0 or x == ay-1 or y == 0 or y == ax-1:
                        tmp = []
                        break
                    tmp.append((x,y))
                    for k in range(6):
                        if x % 2 == 0:
                            nx = x + dx1[k]
                            ny = y + dy1[k]
                        else:
                            nx = x +dx2[k]
                            ny = y +dy2[k]
                        if 0 <= nx < ay and 0 <= ny < ax and arr[nx][ny] == 0 and visited[nx][ny] == 0:
                            queue.append((nx,ny))
                            visited[nx][ny] = 1
                
                for j in tmp:
                    arr[j[0]][j[1]] = 1

search()

cnt = 0
for i in range(ay):
    for j in range(ax):
        if arr[i][j] == 1:
            for k in range(6):
                if i % 2 == 0:
                    nx = i + dx1[k]
                    ny = j + dy1[k]
                else:
                    nx = i +dx2[k]
                    ny = j +dy2[k]
                if 0 <= nx < ay and 0 <= ny < ax:
                    if arr[nx][ny] == 0:
                        cnt +=1
                else:
                    cnt +=1 



print(cnt)