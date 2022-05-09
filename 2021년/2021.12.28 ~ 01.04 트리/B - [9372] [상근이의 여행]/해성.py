import sys

def dfs(start, end):
    visited[start] = True
    if False not in visited:
        global cnt
        return cnt
    else:
        for i in tree[start]:
            if visited[i] == True:
                pass
            else:
                cnt+=1
                visited[i] = True
                dfs(i, end)

tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    # tree = {}
    tree = [[] for _ in range(N+1)]
    visited = [False] *(N+1)
    # print(visited)
    cnt = 0
    # print(tree)
    for i in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        # tree[a] = b
        # tree[b] = a
    # print(tree)
    visited[0] = True
    dfs(1, N)
    print(cnt)