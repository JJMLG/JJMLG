import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    # print(q)
    while q:
        t = q.popleft()
        # print(t)

        for i in t:
            # print(i)
            if visited[i[0]-1] == -1:
                visited[i[0]-1] = visited[i[1]]
                print(visited)


v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
cnt = 0
visited = [-1] * (v+1)

# print(visited)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, len(graph)):
    bfs(graph[i])
# print(graph)