
import sys, heapq




n,d = map(int,input().split())
arr = [[] for _ in range(d+1)]
INF = int(1e9)
distance = [INF]*(d+1)
for j in range(d):
    arr[j].append((j+1,1))

for i in range(n):
    start,end,time = map(int,input().split())
    if end > d:
        continue

    arr[start].append((end,time))


def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for end,length in arr[now]:
            cost = dist + length
            if distance[end] > cost:
                distance[end] = cost
                heapq.heappush(queue,(cost,end))

dijkstra(0)
print(distance)