import heapq
import sys
INF = sys.maxsize # 가상의 최대값

def dijkstra(start):
    q = [] # 방문가능한 지점
    heapq.heappush(q, (0, start)) # 출발점 입력
    dis[start] = 0 # 출발지점은 거리가 0
    while q: # 다익스트라
        d, now = heapq.heappop(q)
        # print(d, now) # 디버깅
        if dis[now] < d: # 최소거리가 될 수 없으면
            continue # 백트래킹
        # print(graph[now]) # 디버깅
        for v, w in graph[now]:
            # 들고 있는 최소거리 + 이동할 거리
            cost = d + w 
            if cost < dis[v]: # 새로운 최소값이면
                dis[v] = cost # 갱신
                # 다음 이동지점에 갱신된 최소값 추가
                heapq.heappush(q, (cost, v))

N, M = map(int, input().split())
# 각 노드에서 이동 가능한 지점들 리스트
graph = [[] for _ in range(N+1)]
dis = [INF]*(N+1) # 각 노드별 최소 이동거리 DP
for _ in range(M):
    a, b, c = map(int, input().split())
    # 양방향 방문가능 노드 추가
    graph[a].append((b, c))
    graph[b].append((a, c))
dijkstra(1) # 1부터 출발
print(dis[N]) # 출력