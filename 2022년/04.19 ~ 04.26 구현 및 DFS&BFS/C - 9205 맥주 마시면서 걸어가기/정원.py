import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([home[0], home[1]]) # 집에서부터
    while q: # 갈 수 있는 편의점이 있는 동안
        x, y = q.popleft() # 출발
        # 목적지에 도착할 수 있으면
        if abs(x - goal[0]) + abs(y - goal[1]) <= 1000:
            print("happy") # 축제에 갈 수 있다
            return # 축제에 갈 수 있으므로 코드 종료
        for i in range(N): # N개의 편의점 중
            if not visited[i]: # 간 적 없는 편의점
                nx, ny = store[i] # 편의점의 좌표
                # 갈 수 있는 편의점이면
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append((nx, ny)) # 편의점 좌표 추가
                    visited[i] = 1 # 편의점 방문처리
    print("sad") # 다 돌아도 못갔네 ㅠㅠ
    return

for t in range(int(input())):
    N = int(input())
    home = list(map(int, input().split()))
    store = []
    for i in range(N): # N개의 편의점
        store.append(tuple(map(int, input().split())))
    goal = list(map(int, input().split()))
    visited = [0 for _ in range(N+1)] #home 제외
    bfs() # 집부터 출발