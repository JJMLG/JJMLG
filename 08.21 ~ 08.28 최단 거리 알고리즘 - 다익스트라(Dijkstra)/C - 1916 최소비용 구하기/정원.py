import sys
import heapq # 탐색 시 가장 작은 값을 탐색하기 위함

input = sys.stdin.readline
INF = int(1e9) # 가상의 최대값

def dijkstra(start):
    distance[start] = 0 # 시작점에서 시작점으로 가는 최단 경로값은 0
    heapq.heappush(Q, (0, start))
    while Q:
        dist, now = heapq.heappop(Q) # 가장 작은 값을 heappop으로 꺼내기
        if dist > distance[goal]: continue # 백트래킹, 목적지가 정해져 있으므로, 이미 구한 목적지 최소 경로값보다 큰 경우는 전부 컷 가능
        for next, weight in data[now]: # 현재 노드에서 갈 수 있는 노드와 가중치들을 순회하면서
            cost = dist + weight # 경로값은 들고 있는 경로값 + 가중치
            if cost < distance[next]: # 더 작은 경로값이 발견되면
                distance[next] = cost # 최소 경로값 갱신
                heapq.heappush(Q, (cost, next)) # 해당 경로와 다음 노드를 heappush로 가장 앞에 추가

V = int(input())
E = int(input())
data = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    data[u].append((v, w)) # 노드 u에서 갈 수 있는 노드v와 그 때의 가중치 w
distance = [INF]*(V+1) # 가상의 최대 경로값 배열
Q = [] # heapq의 메소드만 사용함, deque와 다르게, 일반적인 리스트 선언
start, goal = map(int, input().split())
dijkstra(start) # start부터 출발
print(distance[goal]) # 목적지의 최소 경로값 출력