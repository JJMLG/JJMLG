"""
배열을 탐색하다가 섬을 발견하면
    섬의 개수 ++
    섬을 바다로 만든다 (1 -> 0) # BFS (DFS로 하는데 메모리초과가 계속 남 ㅜㅜ)
    발견한 섬의 개수를 출력
"""
from collections import deque # BFS용 double ended queue


def bfs(y, x): # 섬을 바다로 만드는 BFS함수
    Q.append((y, x))
    while Q:
        y, x = Q.popleft()
        if arr[y][x] == 0:
            continue
        arr[y][x] = 0
        for i in range(8):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<H and 0<=nx<W and arr[ny][nx]:
                Q.append((ny, nx))


dy = [-1, 1, 0, 0, 1, 1, -1, -1] # 대각선 포함한 8방향 델타이동
dx = [0, 0, -1, 1, 1, -1, 1, -1]
while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0: # 테스트케이스 입력 종료조건
        break
    arr = [list(map(int, input().split())) for _ in range(H)] # 지도
    result = 0 # 섬의 개수
    Q = deque()
    for h in range(H):
        for w in range(W):
            if arr[h][w]: # 섬을 발견하면
                bfs(h, w) # 섬을 바다로 만들기
                result += 1 # 섬의 개수 ++
    print(result) # 섬의 개수 출력


# 아래는 재귀함수를 활용한 DFS로 풀었는데
# 메모리초과를 피하지 못했습니다ㅜㅜ
# 재귀를 계속 돌면서 함수 내 메모리를 전부 사용한 것 같은데...
# import sys
# sys.setrecursionlimit(10**9)


# def dfs(y, x): # 섬을 바다로 만들어 주면서 섬 개수 세기
#     if arr[y][x] == 0:
#         return
#     arr[y][x] = 0
#     for i in range(8):
#         ny = y+dy[i]
#         nx = x+dx[i]
#         if 0<=ny<H and 0<=nx<W and arr[ny][nx]:
#             dfs(ny, nx)


# dy = [-1, 1, 0, 0, 1, 1, -1, -1]
# dx = [0, 0, -1, 1, 1, -1, 1, -1]
# while True:
#     W, H = map(int, input().split())
#     if W == 0 and H == 0:
#         break
#     arr = [list(map(int, input().split())) for _ in range(H)]
#     result = 0
#     for h in range(H):
#         for w in range(W):
#             if arr[h][w]:
#                 dfs(h, w)
#                 result += 1
#     print(result)