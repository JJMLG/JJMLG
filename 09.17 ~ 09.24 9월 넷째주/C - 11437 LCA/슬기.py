from collections import deque
import sys
sys.stdin = open('input.txt')

n = int(input())

par = [0] * (n+1)

def dfs(x, dep):
    visit[x] = 1
    d[x] = dep

    for i in graph[x]:
        if visit[i] == 1:
            continue
        par[i] = x
        dfs(i, dep+1)


def parent(a, b):
    while d[a] != d[b]:
        if d[a] < d[b]:
            b = par[b]
        else:
            a = par[a]
    while a != b:
        a = par[a]
        b = par[b]
    return a

graph = [[] for _ in range(n+1)]
d = [0] * (n+1)
visit = [0] * (n+1)
for _ in range(n-1):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

m = int(input())
dfs(1, 0)
for _ in range(m):
    v, w = map(int, input().split())
    print(parent(v, w))