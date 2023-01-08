import sys
import heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline
INF = int(1e9)  #무한을 의미하는 값

city = int(input())
bus = int(input())

distance = [INF] * (city+1)             # 최단거리 담을 테이블
graph = [[] for _ in range(city+1)]     # 노드 연결 정보


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))       # 시작 노드
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)    # 최단거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist:        # 이미 처리된 노드면 무시
            continue                    # 별도의 visited 테이블 필요 없이, 최단 거리 테이블 사용해 방문 여부 확인
        for v, w in graph[now]:         # 선택된 노드와 인접한 노드를 확인
            cost = dist + w
            if cost < distance[v]:      # 선택된 노드를 거쳐 이동하는 것이 더 빠른 경우
                distance[v] = cost
                heapq.heappush(q, (cost, v))



for _ in range(bus):
    start, arrived, cost = map(int, input().split())
    # print(start, arrived, cost)
    graph[start].append((arrived, cost))            # 그래프에 각 출발점이 갈 수 있는 도착점과 비용 넣어주기
    # print(graph)
f_start, f_arrived = map(int, input().split())      # 찾을 시작점, 찾을 도착점
# print(f_start, f_arrived)
dijkstra(f_start)
print(distance[f_arrived])
