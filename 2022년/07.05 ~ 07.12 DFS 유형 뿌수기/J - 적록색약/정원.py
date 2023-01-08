from collections import deque # BFS
from copy import deepcopy # 원본 배열 복사하여 색약 배열로 변경하기 위함


def bfs(arr, y, x, color):
    Q = deque()
    Q.append((y, x))
    while Q:
        y, x = Q.popleft()
        if not arr[y][x]:
            continue
        arr[y][x] = 0
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<N and arr[ny][nx] == color:
                # 탐색범위를 벗어나지 않으면서, 현재 탐색중인 색깔과 같으면
                Q.append((ny, nx))


dy = [-1, 1, 0, 0] # 4방향 델타이동
dx = [0, 0, -1, 1]
N = int(input())
normal_arr = [list(input()) for _ in range(N)] # 원본배열
CB_arr = deepcopy(normal_arr) # 원본 배열 복사하여 색약배열 초기화
for i in range(N): # 적록색약 배열
    for j in range(N):
        if CB_arr[i][j] in 'RG': # 빨강과 초록을 구분할 수 없으므로
            CB_arr[i][j] = 'A' # 임의의 문자 A로 통일
normal = CB = 0 # 일반인, 색약인(color blind) 결과값 초기화
for i in range(N):
    for j in range(N):
        if normal_arr[i][j]: # normal
            bfs(normal_arr, i, j, normal_arr[i][j])
            normal += 1 # 일반인이 볼 수 있는 구역 ++
        if CB_arr[i][j]: # color blind
            bfs(CB_arr, i, j, CB_arr[i][j])
            CB += 1 # 색약인이 볼 수 있는 구역 ++
print(normal, CB) # 출력