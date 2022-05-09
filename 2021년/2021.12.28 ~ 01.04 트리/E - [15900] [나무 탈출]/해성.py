import sys

sys.setrecursionlimit(30000)
N = int(sys.stdin.readline())

tree = [[] for _ in range(N+1)]
parent = [0] * (N+1)
visited = [0] * (N+1)
for i in range(N-1):
    x, y = map(int, sys.stdin.readline().split())
    tree[x].append(y)
    tree[y].append(x)
result = 0
start = 1
visited[start] = 1

def dfs(start):
    for i in tree[start]:
        if visited[i] !=0:

            pass
        else:
            visited[i] = 1
            parent[i] = parent[start]+1
            # print(visited)
            # result -=cnt
            dfs(i)
dfs(1)

result = 0
for i in range(2, N+1):
    if not parent[i]:
        result += visited[i]

if result % 2:
    print('YES')
else:
    print('NO')

