import sys
from heapq import heappush, heappop

input = sys.stdin.readline # 일종의 루틴 같은 것
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1] # 델타이동

def dijkstra():
    heappush(Q, (0, 0, 0)) # change, y, x
    visited[0][0] = 1 # 0, 0 출발
    while Q:
        change, y, x = heappop(Q) # heapq 특성상, 튜플등에선 맨 앞 값을 기준으로 정렬한다
        if y == x == N-1: break # 방을 바꿔가며 어찌저찌 목표지점에 도착
        delta_move(change, y, x) # 4방향 델타이동
    return change # line 11의 change를 의미함, while문을 break했을 때의 change

def delta_move(change, y, x):
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
            visited[ny][nx] = 1
            if room[ny][nx] == 0: # 검은 방 : 통과 불가능, 흰 방으로 바꿈
                heappush(Q, (change+1, ny, nx)) # 방 바꾸면서 가자
            else: # 흰 방 : 통과 가능
                heappush(Q, (change, ny, nx))

N = int(input().rstrip())
room = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
Q = []
print(dijkstra())

"""
핵심
1. visited[i][j]에 대해서, 한 차원 더 방문배열을 만들면서
    "방을 몇 번 바꾸면서 지나왔는가"는 기록할 필요가 없다
    어차피 i,j번 방이, 검은 방을 흰색 방으로 바꿔야 갈 수 있다면
    방을 바꾸지 않고는, change+1 하지 않고는 해당 지점에 닿을 수 없다
2. room[N-1][N-1]에 도달하던 말던 상관없이
    방을 바꾸는 횟수를 최소로 하여 목표까지 도달해야 하기 때문에
    Q[0]에 집어 넣은 change의 값이 작은 것 부터 탐색한다
    그래서 이 문제는 다익스트라다
"""

# https://www.acmicpc.net/problem/2665