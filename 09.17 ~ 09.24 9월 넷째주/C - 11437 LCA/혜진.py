import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**5)

def DFS(curr, dep):
    find[curr] = True
    depth[curr] = dep

    for nn in adj[curr]:
        if find[nn]: continue
        pa[nn] = curr
        DFS(nn, dep + 1)

def LCA(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = pa[a]
        else:
            b = pa[b]
    while a != b:
        a = pa[a]
        b = pa[b]
    return a

N = int(input())
adj = [[] for _ in range(N + 1)]
maxN = 0
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    maxN = max(maxN, max(a, b))

pa = [0] * (maxN + 1)
depth = [0] * (maxN + 1)
find = [0] * (maxN + 1)

DFS(1, 0)
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
