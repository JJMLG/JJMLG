import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0

    while q:
        t = q.popleft()

        for j in graph[t]:
            if visited[j] == -1:
                q.append(j)
                visited[j] = visited[t]+1



n, k = map(int, input().split())

graph = [[] for _ in range(n+1)]

visited = [-1] * (n+1)

for _ in range(k):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)
# print(graph)

confirm = 1
for i in range(1, n+1):
    visited = [-1] * (n + 1)
    bfs(i)
    if (max(visited) > 6) or (-1 in visited[1:]):
        confirm = 0
        break

if confirm:
    print('Small World!')
else:
    print('Big World!')