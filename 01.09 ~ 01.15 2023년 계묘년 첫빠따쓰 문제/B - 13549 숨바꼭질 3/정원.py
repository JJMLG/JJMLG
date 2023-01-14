from heapq import heappush, heappop

N, K = map(int, input().split())
Q = [(0, N)]
visited = [int(1e9)]*(int(1e6)+1)
visited[N] = 0
while Q:
    time, now = heappop(Q)
    go, back, jump = max(0, now+1), max(0, now-1), max(0, now*2)

    if now == K:
        break

    if visited[go] > time+1:
        visited[go] = time+1
        heappush(Q, (time+1, go))

    if visited[back] > time+1:
        visited[back] = time+1
        heappush(Q, (time+1, back))
    
    if visited[jump] > time and jump<=100000:
        visited[jump] = time
        heappush(Q, (time, jump))

print(time)