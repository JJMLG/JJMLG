from collections import deque

A, B, N, M = map(int, input().split())
Q = deque() # BFS
Q.append((N, 0)) # 시작점, 초기 이동횟수
result = 0
visited = [0] * 100001 # 돌다리 방문배열
while Q: # 항상 도달할 수 있는 경우만 주어짐
    now, move = Q.popleft() # 현재 위치, 현재까지 이동한 횟수
    if visited[now]: continue # 방문한 적이 있는 돌다리면 continue
    visited[now] = 1 # 현재 돌다리를 방문함
    if now == M: # 목적지에 도착했을 때
        result = move # result = 가지고 있는 이동횟수
        break # while문 종료
    nexts = [now-1, now+1, now-A, now+A, now-B, now+B, now*A, now*B] # 6가지 경우의 다음 이동 돌다리
    for next in nexts:
        if 0<=next<=100000 and not visited[next]: Q.append((next, move+1)) # 돌다리 범위를 만족하며, 방문한 적 없는 돌다리 일 때
print(result)