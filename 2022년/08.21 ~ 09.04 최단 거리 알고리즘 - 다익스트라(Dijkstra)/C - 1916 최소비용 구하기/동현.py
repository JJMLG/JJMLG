import sys
import heapq

INF = int(1e9)


n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    u,v,w = map(int,input().split())
    arr[u].append([v,w])

def dijkstra(start):
    q = []
    heapq.heappush(q,[0,start])
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = dist +i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])

s,e = map(int,input().split())
dijkstra(s)

print(distance[e])