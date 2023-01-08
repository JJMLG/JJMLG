import sys
from collections import deque

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0
result = []
while True:
    # pprint(arr)
    # print(result)
    queue = deque()
    queue.append([0,0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    cnt = 0
   
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                visited[nx][ny] = -1
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append([nx,ny])
                
                visited[nx][ny] = 1
   
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] == -1:
                cnt +=1 
                arr[i][j] += visited[i][j]
    result.append(cnt)
    if cnt == 0:
        print(ans)
        print(result[-2])
        exit()
    ans += 1 
    
# pprint(visited)