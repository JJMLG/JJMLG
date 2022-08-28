import sys, heapq

input = sys.stdin.readline
INF = int(1e9) # 가상의 최대 거리

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(Q, (0, start))
    while Q:
        dist, now = heapq.heappop(Q)
        for next, weight in data[now]: # weight = 1, 출력용으로만 사용
            cost = dist + 1
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(Q, (cost, next))

V, E, K, X = map(int, input().split())
data = [[] for _ in range(V+1)]
for _ in range(E):
    A, B = map(int, input().split())
    data[A].append((B, 1)) # 가중치 = 1
distance = [INF] * (V+1) # 가상의 최대 거리 배열
Q = []
dijkstra(X) # X부터 시작하여 다른 도시까지 이동하는 최소 거리 배열 값 구하기
flag = False # K거리인 도시가 있는지 체크하는 플래그
for i in range(1, len(distance)):
    if distance[i] == K:
        print(i) # 도시 번호 출력
        flag = True # 최소 거리가 K에 해당하는 도시가 있음
if not flag: # 해당하는 도시가 없을 경우
    print(-1)