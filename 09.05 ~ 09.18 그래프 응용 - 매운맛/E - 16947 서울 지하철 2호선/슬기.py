import sys
sys.stdin = open('input.txt')
from collections import deque
sys.setrecursionlimit(100000)

def dfs(start, idx, cnt):
    global cycle

    if start == idx and cnt >= 2:
        cycle = 1
        return

    visited[idx] = 1

    for i in graph[idx]:
        if not visited[i]:
            dfs(start, i, cnt + 1)
        elif i == start and cnt >= 2:
            dfs(start, i, cnt)


def bfs():
    global check

    q = deque()

    for j in range(n):
        if cycle_station[j]:
            check[j] = 0
            q.append(j)

    while q:
        now = q.popleft()

        for x in graph[now]:
            if check[x] == -1:
                q.append(x)
                check[x] = check[now] + 1

    for y in check:
        print(y, end = ' ')


n = int(input())
graph = [[] for _ in range(n)]
cycle_station = [0] * n
check = [-1] * n

for _ in range(n):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


for i in range(n):
    visited = [0] * n
    cycle = 0
    dfs(i, i, 0)

    if cycle:
        cycle_station[i] = 1

bfs()