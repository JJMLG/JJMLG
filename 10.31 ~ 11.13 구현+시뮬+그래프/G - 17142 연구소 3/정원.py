import sys
from itertools import combinations as comb
from collections import deque

input = sys.stdin.readline
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def spread_virus(viruses):
    new_arr = [[-1]*N for _ in range(N)] # 문제의 예시처럼, 바이러스가 퍼진 시간을 기록할 배열
    # deactivate other viruses
    for i in range(N):
        for j in range(N):
            if new_arr[i][j] == 2 and (i, j) not in viruses:
                new_arr[i][j] = 3
    Q = deque()
    visited = [[0]*N for _ in range(N)]
    for y, x in viruses: 
        Q.append((y, x))
        new_arr[y][x] = 0
        visited[y][x] = 1
    while Q:
        y, x = Q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                if arr[ny][nx] != 1:
                    Q.append((ny, nx))
                    new_arr[ny][nx] = new_arr[y][x]+1
                    visited[ny][nx] = 1
    all_spreaded_check(new_arr, visited)

def all_spreaded_check(arr, visited):
    global result
    new_wall = 0
    max_time = 0
    for i in range(N):
        for j in range(N):
            if (i, j) not in virus_coordinates: # 바이러스의 시간은 카운트하지 않는다
                max_time = max(max_time, arr[i][j])
            if visited[i][j] == 0:
                new_wall += 1
    if wall == new_wall: # 
        result = min(max_time, result)

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
virus_coordinates = []
wall = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_coordinates.append((i, j))
        if arr[i][j] == 1:
            wall += 1
virus_combinations = list(comb(virus_coordinates, M))
result = int(1e9) # 가상의 최소값
for viruses in virus_combinations: # 매 바이러스 조합에 대해
    spread_virus(viruses) # 바이러스 퍼뜨리기
if result == int(1e9): result = -1 # 한 번도 바이러스가 다 퍼지지 못했다면 -1
print(result)

# 문제가 좀 이상합니다....;;
