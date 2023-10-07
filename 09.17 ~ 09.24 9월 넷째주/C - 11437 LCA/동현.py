import sys
sys.setrecursionlimit(100000)

n = int(input())
parent = [0] * (n + 1)      # 각 노드의 부모 노드 정보
d = [0] * (n + 1)           # 각 노드까지의 깊이
visited = [0] * (n + 1)     # 방문 여부
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 루트 노드부터의 깊이 구하기
def dfs(x, depth):
    visited[x] = True
    d[x] = depth

    for node in graph[x]:
        if visited[node]:
            continue
        parent[node] = x
        dfs(node, depth + 1)


# 최소 공통 조상 찾기
def lca(a, b):
    # 깊이 맞추기
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 노드 맞추기
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


dfs(1, 0)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))