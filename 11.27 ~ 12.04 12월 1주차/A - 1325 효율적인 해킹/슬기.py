import sys
sys.stdin = open('input.txt')
from collections import deque

n, m = map(int, input().split())

graph = [[] * (n+1) for _ in range(n+1)]

res = []
max_cnt = 0
def bfs(x):
    q = deque(x)
    cnt = 1
    visited = [0] * (n + 1)

    while q:
        t = q.popleft()
        # print(t)
        for j in graph[t]:
            # print(i)
            if visited[j] == 0:
                visited[j] = 1
                q.append(j)
                cnt += 1
    return cnt
    # print(visited)

for _ in range(m):
    a, b = map(int, input().split())
    # print(a, b)
    # graph[a].append(b)
    graph[b].append(a)


    # print(graph)
for i in range(1, n+1):
    cnt = bfs(graph[i])
# print(res)
    if cnt > max_cnt:
        max_cnt = cnt
    res.append([i, cnt])

for i, cnt in res:
    if cnt == max_cnt:
        print(i, end=' ')