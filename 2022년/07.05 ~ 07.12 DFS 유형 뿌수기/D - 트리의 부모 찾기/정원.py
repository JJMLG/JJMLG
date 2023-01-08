import sys
sys.setrecursionlimit(99999)


def dfs(i):
    for n in nodes[i]:
        if not parents[n]:
            parents[n] = i
            dfs(n)


N = int(input())
nodes = [[] for _ in range(N+1)]
parents = [0] * (N+1)
for n in range(N-1):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)
dfs(1)
for p in parents[2:]: print(p)