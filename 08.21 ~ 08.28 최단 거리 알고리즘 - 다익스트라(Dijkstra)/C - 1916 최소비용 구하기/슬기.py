import sys, heapq
sys.stdin = open('input.txt')

n = int(input())
m = int(input())

INF = int(1e9)
distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


for _ in range(m):
    depart, arrive, cost = list(map(int, input().split()))

    graph[depart].append((arrive, cost))
# print(graph)
    # print(depart, arrive, cost)
start, end = list(map(int, input().split()))
dijkstra(start)
print(distance[end])
# for i in range(n+1):
