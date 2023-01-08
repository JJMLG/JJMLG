from collections import deque

N, M, K = map(int, input().split())
# 모눈종이를 전부 1로 채우고, 직사각형으로 채워지는 곳을 0으로 바꿈
arr = [[1]*M for _ in range(N)]
for k in range(K):
    area = list(map(int, input().split()))
    for i in range(area[1], area[3]):
        for j in range(area[0], area[2]):
            arr[i][j] = 0
result = [] # 넓이를 담을 리스트
# 델타이동
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque() # BFS
cnt = 0 # 넓이(영역)의 개수
# 모눈종이를 돌다가
for n in range(N):
    for m in range(M):
        if arr[n][m]: # 분리된 영역이 있으면
            q.append((m, n)) # 출발
            square = 0 # 넓이값 초기화
            while q: # BFS
                tmp = q.popleft()
                x, y = tmp[0], tmp[1]
                if arr[y][x]:
                    arr[y][x] = 0 # 방문 처리
                    square += 1 # 넓이 계산
                    for i in range(4): # 델타이동 하였을 때
                        # 모눈종이를 벗어나지 않으며, 이웃한 분리된영역일 경우
                        if (0 <= x+dx[i] < M) and (0 <= y+dy[i] < N) and arr[y+dy[i]][x+dx[i]]:
                            q.append((x+dx[i], y+dy[i])) # 탐색점 추가
            result.append(square) # 영역의 넓이 리스트에 저장
            cnt += 1 # 영역 한 개 확인
result.sort() # 넓이 오름차순으로 정렬
# 출력
print(cnt)
print(*result)