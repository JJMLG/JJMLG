import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def delta_move(y, x, D, mine, Q, visited):
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
            if mine[ny][nx]<=D: # 공기or캘 수 있는 광물
                visited[ny][nx] = 1
                Q.append((ny, nx))
            else: # 캘 수 없는 광물
                visited[ny][nx] = 1 # 방문하였으나 캘 수 없었다

def BFS(D): # 채굴기의 성능 D
    mine = deepcopy(arr) # 광__산
    mineral = 0 # 채굴기 성능이 D일때 캘 수 있는 광물의 수 초기화
    visited = [[0]*M for _ in range(N)] # 광산 방문배열
    Q = deque()
    Q.append((0, 0)) # 공기층을 추가하였으니, 0,0부터 시작
    visited[0][0] = 1
    while Q: # 캘 수 있는 광물 체크
        y, x = Q.popleft()
        if mine[y][x]: # 광물이면
            mine[y][x] = 0 # 캐고
            mineral += 1 # 저장
        delta_move(y, x, D, mine, Q, visited)
    return mineral # 채굴기 성능이 D일때 캘 수 있는 광물 수

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1] # 4방향 델타이동
N, M, K = map(int, input().rstrip().split())
M += 2
# 배열 테두리에 공기층 생성
arr = [[0]*M] + [[0]+list(map(int, input().rstrip().split()))+[0] for _ in range(N)]
N += 1
# 1<=N,M<=1000, 1<=K<=1e6
# 채굴기의 성능을 1부터 +1하면서 전수조사 할 수 없다
# 채굴기의 성능 이분탐색 필요
result = int(1e7)
start, end = 1, int(1e7)
while start<=end:
    mid = (start+end) // 2
    mineral = BFS(mid) # 현재 채굴기의 성능으로 광물을 채굴해보자
    if mineral>=K: # K개의 광물을 충분히 채굴할 수 있음, 성능 D를 좀 더 높여도 됌
        end = mid-1
        result = min(result, mid)
    else: # 현재 성능으로는 K개의 광물을 채굴할 수 없음
        start = mid+1
print(result)

"""
이분탐색과 BFS의 혼합문제다
BFS를 함수화시켜서 이분탐색안에 넣는 편이 좋다
고난이도 문제로 오면서 "코드 구조화"가 중요해지는 것 같다
탭 3번정도 단위로 끊어서 함수화 시키자
브론즈 실버등, 간단한 문제도 함수화(구조화)연습을 많이 하자
"""

# https://www.acmicpc.net/problem/15573