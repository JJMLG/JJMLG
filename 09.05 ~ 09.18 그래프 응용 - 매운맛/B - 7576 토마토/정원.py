from collections import deque # BFS

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1] # delta 이동
M, N = map(int, input().split()) # M부터 받는 거, 낚시 주의
arr = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1: # 첫 날 토마토인 좌표들 추가
            Q.append((i, j, 0)) # y, x, day
            arr[i][j] = 0
result = 0
while Q: # BFS
    y, x, day = Q.popleft() # day를 추가하면서 가장 마지막에 나온 day를 잡을 것
    if arr[y][x] == 1: continue # 다른 토마토를 통해서 이미 익은 토마토
    arr[y][x] = 1 # 잘 익은 토마토
    result = max(result, day) # 더 오랜시간이 걸려서 익은 토마토가 있으면 갱신
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i] # 전후좌우 토마토
        if 0<=ny<N and 0<=nx<M and arr[ny][nx] == 0:
            Q.append((ny, nx, day+1)) # 다음 날에 이 토마토는 익는다
for i in range(N):
    if result == -1: break # 모든 토마토가 익을 수 없었다? -> 종료
    for j in range(M):
        if arr[i][j] == 0: # 충분한 시간이 흘렀는데 안익은 토마토가 있다?
            result = -1 # 모든 토마토가 익을 수 없었다
            break
print(result)

# https://www.acmicpc.net/problem/7576