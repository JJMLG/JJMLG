import sys
import heapq

dx = [-1,1,0,0]
dy = [0,0,-1,1]

INF = int(1e9)


def dijkstra():
    global result
    q = []
    distance = [[INF]*n for _ in range(n)]
    heapq.heappush(q,[arr[0][0],0,0])
    distance[0][0] = 0
    while q:
     
        dist, x,y = heapq.heappop(q)
        if x == n-1 and y == n-1:
            result = dist
           
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                nw = dist + arr[nx][ny]
                if nw < distance[nx][ny]:
                    distance[nx][ny] = nw
                    heapq.heappush(q, [nw, nx, ny])

cnt =1 
while True:
    result = 0
    n = int(input())
    if n == 0:
        break
  
    arr = [list(map(int, input().split())) for _ in range(n)]
    dijkstra()
    print(f'Problem {cnt}: {result}')
    cnt += 1

