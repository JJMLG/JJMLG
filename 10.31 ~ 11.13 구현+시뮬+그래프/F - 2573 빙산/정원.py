import sys
from collections import deque

input = sys.stdin.readline
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1] # 4방향 델타이동

def count_iceberg(): # 빙산의 개수 확인
    Q = deque()
    visited = [[0]*M for _ in range(N)]
    iceberg = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]: # 처음 빙산을 발견하면
                iceberg += 1 # 빙산 개수 ++
                Q.append((i, j)) # 해당 점을 Q에 담아서
                visited[i][j] = 1
                while Q: # 처음 빙산을 발견한 점에서부터 이어지는 빙산을 방문처리한다
                    y, x = Q.popleft()
                    for k in range(4):
                        ny, nx = y+dy[k], x+dx[k]
                        if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and arr[ny][nx]:
                            Q.append((ny, nx))
                            visited[ny][nx] = 1
    return iceberg # 빙산의 덩어리 개수

def check_seawater(): # 바닷물 확인
    tmp_Q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: # 바닷물인가요?
                tmp_Q.append((i, j))
    return tmp_Q # 바닷물을 담고 있는 Q

def melt_iceberg(seawater_Q): # 빙산 녹이기
    while seawater_Q: # 확인한 바닷물 주변의 빙산을 녹인다
        y, x = seawater_Q.popleft()
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            if 0<=ny<N and 0<=nx<M and arr[ny][nx]>0:
                arr[ny][nx] -= 1

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
result = 0 # 결과값 초기화
while count_iceberg() == 1: # 빙산이 한 덩이일 때
    result += 1 # 시간 ++
    seawater_Q = check_seawater() # 바닷물 체크
    melt_iceberg(seawater_Q) # 바닷물 주변 녹이기
# while문이 종료되었다면 경우는 두가지다
# 1. 두 덩이로 녹았거나
# 2. 빙산이 통째로 녹았거나
if count_iceberg() == 0: print(0) # 두 덩이로 나뉘지 않고 동시에 녹아버렸다면 0을 출력
else: print(result) # 아니라면, 두 덩이로 분리되는 최초의 시간 출력

# https://www.acmicpc.net/problem/2573