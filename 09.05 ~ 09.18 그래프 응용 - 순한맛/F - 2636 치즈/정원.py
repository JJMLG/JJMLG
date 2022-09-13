from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [0, int(1e9)] # [녹는데 걸리는 시간, 다 녹기 한 시간 전 남은 치즈 수]
while True:
    melt = True # 다 녹았는지 확인할 것
    cheese = 0 # 지금 남아있는 치즈 수
    for i in range(N):
        for j in range(M):
            if arr[i][j]: # 하나라도 안 녹은 치즈가 있다면
                melt = False # 다 녹은 것은 아니지
                cheese += 1 # 치즈 개수 증가
    if melt: # 다 녹았다면
        for r in result: print(r) # 출력
        break
    else: # 다 안녹았다면 녹이러 가자!
        Q, cheese_Q = deque(), deque() # 배열탐색 deque, 녹일 치즈만 담을 deque
        visited = [[0]*M for _ in range(N)]
        Q.append((0, 0)) # 배열의 가장자리는 무조건 공기이다
        visited[0][0] = 1 
        while Q:
            y, x = Q.popleft()
            for k in range(4):
                ny, nx = y+dy[k], x+dx[k] # 상하좌우
                if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
                    visited[ny][nx] = 1 # 치즈든 공기든, 탐색할 것
                    if arr[ny][nx]: # 치즈
                        cheese_Q.append((ny, nx)) # 녹일 치즈
                    else: # 공기
                        Q.append((ny, nx)) # 다음 탐색할 공기
        while cheese_Q: # 치즈를 녹이자
            y, x = cheese_Q.popleft()
            arr[y][x] = 0 # 치즈가 녹는다
        result[0] += 1 # 한 시간 경과
        result[1] = min(result[1], cheese) # 배열의 치즈들은 녹았지만, cheese는 녹기 전 치즈 수를 가지고 있다

"""
핵심
1. 공기를 기준으로 주변 치즈를 녹인다
2. 녹이면서 진행하지 말고
    녹일 치즈들을 한 데 모아, 한 번에 녹인다
"""