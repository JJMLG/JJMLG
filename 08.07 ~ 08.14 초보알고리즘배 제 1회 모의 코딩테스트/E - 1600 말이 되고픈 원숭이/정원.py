import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0] # delta y
dx = [0, 0, -1, 1] # delta x
ky = [-2, -1, 1, 2, 2, 1, -1, -2] # knight y
kx = [1, 2, 2, 1, -1, -2, -2, -1] # knight x

def bfs():
    Q = deque()
    Q.append((0, 0, K, 0)) # y, x, k, move
    # 3차원 방문배열
    # 만약 K가 2일 때, 해당 좌표까지 나이트 이동을 0번 혹은 1번 혹은 2번 사용하여
    # 해당 좌표에 도착할 수 있는지 체크하기 위함
    visited = [[[False]*(K+1) for _ in range(W)] for _ in range(H)] 
    # 아래 코드에서 방문 좌표를 추가하면서 방문처리 할 것이므로
    # 시작 점 방문 처리
    visited[0][0][K] = True 
    while Q: # 탐색할 좌표가 있을 때
        y, x, k, move = Q.popleft() # 세로, 가로, 남은 나이트 이동 횟수, 이동한 횟수
        if y == H-1 and x == W-1: # 도착했다면
            return move # 그 때의 이동 횟수
        if k > 0: # 나이트 이동 횟수가 남아있을 때
            for i in range(8):
                ny = y+ky[i] # 나이트 이동 y
                nx = x+kx[i] # 나이트 이동 x
                # 범위 안에 있고, 장애물이 아니면서, 나이트이동으로 탐색할 수 있다면
                if 0<=ny<H and 0<=nx<W and not arr[ny][nx] and not visited[ny][nx][k-1]:
                    # 해당 좌표를 탐색할 것이며
                    # 아직 나이트 이동을 k-1번 할 수 있습니다
                    visited[ny][nx][k-1] = True 
                    Q.append((ny, nx, k-1, move+1))
        for i in range(4):
            ny = y+dy[i] # 델타 이동 y
            nx = x+dx[i] # 델타 이동 x
            # 범위 안에 있고, 장애물이 아니면서
            # 현재 사용가능한 나이트이동의 횟수로 해당 좌표를 방문한 적이 없을 때
            if 0<=ny<H and 0<=nx<W and not arr[ny][nx] and not visited[ny][nx][k]:
                # 해당 좌표를 탐색할 것이며
                # 나이트 이동을 사용하지 않고 탐색합니다
                # 여전히 k번의 나이트 이동을 사용할 수 있습니다
                visited[ny][nx][k] = True
                Q.append((ny, nx, k, move+1))
    return -1 # 도착할 수 없음

K = int(input())
W, H = map(int, input().split())
arr = tuple(tuple(map(int, input().split())) for _ in range(H)) # 시간 단축을 위한 tuple (list보다 빠름, 아마도..?)
print(bfs())


"""
시간 : 120분, 미해결, 정답 풀이 확인 

풀이
    나이트이동이 가능하다고 해서 아무때나 그리디하게 적용하게 되면 오답이다
    세로 가로 에서 하나 더 추가한 3차원 방문배열이 필요하다
    방문 배열의 해당 좌표에 몇번의 나이트 이동으로 도달하였는지 기록하며 진행한다
    나이트이동과 그냥 이동을 통한 탐색을 동시에 진행한다

반례 모음

1
6 6
0 0 1 1 0 0
1 1 1 0 0 0
0 0 1 1 0 0
1 0 1 1 1 1
1 0 0 1 1 1
0 0 0 0 0 0
answer : 8

2
6 6
0 0 1 1 0 0
1 1 1 0 0 0
0 0 1 1 0 0
1 0 1 1 1 1
1 0 0 1 1 1
0 0 0 0 0 0
answer : 6

1
2 3
0 1
1 1
1 0
answer : 1

4
6 6
0 0 1 1 0 0
1 1 1 0 0 0
0 0 1 1 0 0
1 0 1 1 1 1
1 0 0 1 1 1
0 0 0 0 0 0
answer : 4

3
4 5
0 1 1 1
1 1 0 1
1 1 1 1
1 1 1 0
1 1 1 0
answer : 3

1
5 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 0
answer : 6

1
4 4
0 0 1 1
0 0 1 1
0 0 1 1
1 1 1 0
answer : 4
"""


# 쾅
# from collections import deque

# K = int(input())
# W, H = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(H)]
# result = -1
# K_dy = [-2, -1, 1, 2, 2, 1, -1, -2] # Knight dy
# K_dx = [1, 2, 2, 1, -1, -2, -2, -1] # Knight dx
# dy = [-1, 1, 0, 0] # 나이트 이동 이후 델타 dy
# dx = [0, 0, -1, 1] # 나이트 이동 이후 델타 dx
# Q = deque()
# Q.append((H-1, W-1, 0, 0)) # (y, x, K_cnt, move)
# visited = [[0]*W for _ in range(H)] # 방문배열
# K_visited = [[0]*W for _ in range(H)] # 나이트 이동 방문배열
# visited[H-1][W-1] = 1
# K_visited[H-1][W-1] = 1
# tmp = int(1e9) # 가상의 최소값
# while Q:
#     y, x, K_cnt, move = Q.popleft()
#     if y == 0 and x == 0: # 도착했을 경우
#         if move < tmp: tmp = move
#         continue
#     if visited[y][x]: continue
#     if K_cnt < K: # 나이트 이동을 할 기회가 남아있을 때
#         for i in range(8):
#             ny = y + K_dy[i]
#             nx = x + K_dx[i]
#             # 이동하려는 좌표가 범위안에 있고, 방문한 적이 없고, 장애물이 아닐 때
#             if 0<=ny<H and 0<=nx<W and not K_visited[ny][nx] and not arr[ny][nx]:
#                 Q.append((ny, nx, K_cnt+1, move+1))
#                 K_visited[ny][nx] = 1
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         # 이동하려는 좌표가 범위안에 있고, 방문한 적이 없고, 장애물이 아닐 때
#         if 0<=ny<H and 0<=nx<W and not visited[ny][nx] and not arr[ny][nx]:
#             Q.append((ny, nx, K_cnt, move+1))
#             visited[ny][nx] = 1
# for v in visited: print(v)
# print(tmp if tmp != int(1e9) else result)


# 쾅쾅
# from collections import deque

# K = int(input())
# W, H = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(H)]
# result = -1
# K_dy = [-2, -1, 1, 2, 2, 1, -1, -2] # Knight dy
# K_dx = [1, 2, 2, 1, -1, -2, -2, -1] # Knight dx
# dy = [-1, 1, 0, 0] # 나이트 이동 이후 델타 dy
# dx = [0, 0, -1, 1] # 나이트 이동 이후 델타 dx
# Q = deque()
# Q.append((H-1, W-1, 0, 0)) # (y, x, K_cnt, move)
# visited = [[0]*W for _ in range(H)] # 방문배열
# tmp = int(1e9) # 가상의 최소값
# while Q:
#     y, x, K_cnt, move = Q.popleft()
#     if y == 0 and x == 0: # 도착했을 경우
#         tmp = move
#         # print(K_cnt, K)
#         if K_cnt < K: tmp -= (K-K_cnt)*2
#         break
#     if visited[y][x]: continue
#     visited[y][x] = 1
#     blocked = True
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         # 이동하려는 좌표가 범위안에 있고, 방문한 적이 없고, 장애물이 아닐 때
#         if 0<=ny<H and 0<=nx<W and not visited[ny][nx] and not arr[ny][nx]:
#             Q.append((ny, nx, K_cnt, move+1))
#             blocked = False
#     for i in range(8):
#         ny = y + K_dy[i]
#         nx = x + K_dx[i]
#         if ny == 0 and nx == 0:
#             Q.append((ny, nx, K_cnt+1, move+1))
#         elif blocked and K_cnt < K:
#             # 이동하려는 좌표가 범위안에 있고, 방문한 적이 없고, 장애물이 아닐 때
#             if 0<=ny<H and 0<=nx<W and not visited[ny][nx] and not arr[ny][nx]:
#                 Q.append((ny, nx, K_cnt+1, move+1))
# # for v in visited: print(v)
# print(tmp if tmp != int(1e9) else result)