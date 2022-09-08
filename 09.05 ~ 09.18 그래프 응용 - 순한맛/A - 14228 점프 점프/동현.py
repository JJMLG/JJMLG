import sys
from collections import deque

n = int(input())
ls = list(map(int,input().split()))
s = int(input())

visited = [0]*n


queue = deque()
queue.append(s)

while queue:
    t = queue.popleft()
    visited[t-1] = 1
    if 0 <= t+ls[t-1]-1 < n and visited[t+ls[t-1]-1] == 0:
        queue.append(t+ls[t-1])
    if 0 <= t-ls[t-1]-1 < n and visited[t-ls[t-1]-1]  == 0:
        queue.append(t-ls[t-1])

print(sum(visited))
