import sys
sys.setrecursionlimit(10**6)

def dfs(x):

    for i in tree[x]:
        if visited[i] == False:
            visited[i] = True
            parent[i] = x
            dfs(i)

N = int(input())

tree = [[] for _ in range(N+1)]
parent = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

visited[0] = True

dfs(1)

for i in range(2, N+1):
    print(parent[i])
