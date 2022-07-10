import sys
from collections import deque
sys.stdin=open('input.txt')


dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
queue = deque()
result = []
maxx = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt += 1
            
            queue.append([i,j])
            tmp = 0 
            arr[i][j] = -1
            while queue:
                x,y = queue.popleft()
                
                tmp += 1
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                        arr[nx][ny] = -1
                        queue.append([nx,ny])
            if tmp >= maxx:
                maxx = tmp

print(cnt)
print(maxx)
