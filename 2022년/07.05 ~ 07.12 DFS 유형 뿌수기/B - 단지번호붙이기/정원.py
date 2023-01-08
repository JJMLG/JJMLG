from collections import deque


def bfs(y, x): # 단지 내 가구 수 탐색 BFS
    Q.append((y, x))
    cnt = 0
    while Q:
        y, x = Q.popleft()
        if arr[y][x] == 0: # Q에 넣어놓은 사이에 탐색을 마친 경우라면
            continue # 컨티뉴
        arr[y][x] = 0 # 해당 위치 탐색 완료
        cnt += 1 # 단지 내 가구 수 ++
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<N and arr[ny][nx]: 
                # 지도의 범위를 벗어나지 않으면서 이웃한 단지이면
                Q.append((ny, nx))
    return cnt # 단지 내 가구 수 반환


dy = [-1, 1, 0, 0] # 상하좌우 4방향 델타이동
dx = [0, 0, -1, 1]
N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
result = [0] # 단지 수 0으로 초기화
Q = deque()
for i in range(N):
    for j in range(N):
        if arr[i][j]: # 단지를 발견하면
            result.append(bfs(i, j)) # 탐색한 단지내 가구수 추가
            result[0] += 1 # 단지 수 ++
print(result[0]) # 단지 수 출력
for r in sorted(result[1:]): print(r) # 단지내 가구수를 오름차순으로 출력