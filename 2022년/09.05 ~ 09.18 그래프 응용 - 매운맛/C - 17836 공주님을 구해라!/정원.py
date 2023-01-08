import sys
from collections import deque

input = sys.stdin.readline
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

N, M, T = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
distance = int(1e9) # 임의의 거리 최대값
Q = deque()
if arr[0][0] == 2: distance = N+M-2 # 시작부터 그람인 경우, 무지성 택시거리 이동
else: # 시작이 그람은 아닌 경우
    Q.append((0, 0, 0)) # move, y, x
    visited[0][0] = 1
while Q:
    move, y, x = Q.popleft()
    if y == N-1 and x == M-1: distance = min(distance, move) # 공주님한테 도착했을 때 걸린 시간 갱신
    for i in range(4): # 델타 이동
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and arr[ny][nx] != 1: # 방문한 적이 없으며, 마법벽이 아닐 때
            Q.append((move+1, ny, nx)) # 빈 방이든 그람이든 일단 탐색
            visited[ny][nx] = 1
            if arr[ny][nx] == 2: # 그람인 경우
                gram = move+1 + (N+M-2-ny-nx) # 무지성 택시이동, 왔던 길 무시 가능
                distance = min(distance, gram) # 돌고 돌아 그람을 줍는 경우는 배제된다, BFS이니까!
print(distance if distance<=T else 'Fail') # T시간 이내에 공주님을 구할 수 있습니까?

"""
그람을 주운 자리에서 무지성 택시거리로 이동 가능
택시거리 : 두 좌표 (x1, y1), (x2, y2)의 가로+세로
    abs(x1-x2) + abs(y1-y2)
"""

# https://www.acmicpc.net/problem/17836