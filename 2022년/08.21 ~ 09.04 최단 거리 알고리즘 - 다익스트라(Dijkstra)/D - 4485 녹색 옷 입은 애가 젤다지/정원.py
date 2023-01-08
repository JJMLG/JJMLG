import sys
import heapq # 탐색 시 가장 작은 값을 탐색하기 위함

input = sys.stdin.readline
INF = int(1e9) # 가상의 최대값
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def dijkstra(y, x):
    global result
    heapq.heappush(Q, (y, x, arr[y][x]))
    visited[y][x] = arr[y][x]
    while Q:
        y, x, dist = heapq.heappop(Q)
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<N and 0<=nx<N:
                cost = dist + arr[ny][nx]
                if cost < visited[ny][nx]:
                    visited[ny][nx] = cost
                    heapq.heappush(Q, (ny, nx, cost))

case = 0
while True:
    case += 1
    N = int(input())
    if N == 0: break
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[INF]*N for _ in range(N)]
    result = INF
    Q = []
    dijkstra(0, 0)
    print(f'Problem {case}: {visited[N-1][N-1]}')

"""
최소 경로값을 저장하는 배열 생성
모든 지점에 대해 최소 경로값을 구하며 진행
도착점 arr[N-1][N-1]의 최소 경로값을 출력
heapq 자체의 빠른 속도만을 이용하였고
별도의 백트래킹문은 넣지 않음
DP처럼 모든 지점의 최소 경로값을 구하였음
"""