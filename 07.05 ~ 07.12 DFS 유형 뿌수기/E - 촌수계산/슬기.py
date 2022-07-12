import sys
sys.setrecursionlimit(99999)
sys.stdin = open('input.txt')


def dfs(x, y, G, cnt):
    global result

    if x == y:

        result = cnt
        return

    # 같은 부모가(루트) 있으면 촌수 +1씩 해주기;

    for k in G[x]:
        if visited[k] == 0:
            visited[k] = 1
            # cnt += 1
            # print(',,')
            dfs(k, y, G,cnt+1)


n = int(input())

find1, find2 = map(int, input().split())
# print(find1, find2)
m = int(input())

g = [[] for _ in range(n+1)]
visited = [0] * (n+1)
# print(g)
cnt = 0
result = 0
for _ in range(m):
    parent, child = map(int, input().split())
    # print(parent, child)
    g[parent].append(child)
    g[child].append(parent)

visited[find1] = 1

dfs(find1, find2, g,cnt)
if result == 0:
    print(-1)
else:
    print(result)
