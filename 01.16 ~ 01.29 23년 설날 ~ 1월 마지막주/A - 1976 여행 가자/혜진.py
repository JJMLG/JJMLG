from collections import deque

N = int(input())
M = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(lambda x:int(x) - 1, input().split()))
ans = 'YES'

for i in range(M - 1):
    flag = False
    
    Q = deque([plan[i]])
    vis = [0] * N
    vis[plan[i]] = 1

    while Q:
        v = Q.popleft()
        if v == plan[i + 1]:
            flag = True
            break

        for j in range(N):
            if adj[v][j] and not vis[j]:
                vis[j] = 1
                Q.append(j)

    if not flag:
        ans = 'NO'
        break

print(ans)
