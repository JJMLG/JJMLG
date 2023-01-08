from collections import deque

def bfs(i):
    Q = deque([i])
    cnt = 1 # i번 컴퓨터를 해킹하면서 bfs 시작
    visited = [0]*(N+1)
    visited[i] = 1
    while Q:
        i = Q.popleft()
        for nxt in arr[i]:
            if not visited[nxt]:
                visited[nxt] = 1
                Q.append(nxt)
                cnt += 1
    return cnt

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)

result = [0]*(N+1)
for i in range(1, N+1):
    result[i] = bfs(i)

maxx = max(result)
for i in range(N+1):
    if result[i] == maxx:
        print(i, end=' ')