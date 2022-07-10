from collections import deque


def bfs(y, x):
    Q.append((y, x))
    global maxx # 가장 넓이가 넓은 그림의 넓이 전역변수 선언
    tmp = 0
    while Q:
        y, x = Q.popleft()
        if arr[y][x] == 0: # 이전에 이미 탐색한 지점이면
            continue # 컨티뉴
        arr[y][x] = 0
        tmp += 1 # 해당 그림의 넓이 ++
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M and arr[ny][nx]:
                Q.append((ny, nx))
    if tmp > maxx: # 가장 넓이가 넓은 그림을 새로 발견하였으면
        maxx = tmp # 갱신


dy = [-1, 1, 0, 0] # 상하좌우 4방향 델타이동
dx = [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = maxx = 0 # 그림의 수, 최대 넓이 초기화
Q = deque()
for n in range(N):
    for m in range(M):
        if arr[n][m]: # 그림을 발견하면
            bfs(n, m) # BFS 탐색
            result += 1 # 그림의 수 ++
print(result)
print(maxx) 