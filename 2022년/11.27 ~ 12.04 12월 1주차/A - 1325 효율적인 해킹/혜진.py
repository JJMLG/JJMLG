from collections import deque


def bfs(s):
    vi = [0] * (N + 1)
    vi[s] = 1
    Q = deque([s])
    while Q:
        v = Q.popleft()
        for w in adj[v]:
            if not vi[w]:
                vi[w] = 1
                Q.append(w)

    return sum(vi)      # 해킹 가능한 컴퓨터의 수


N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[b].append(a)

ans = []                # 컴퓨터 번호 배열
cnt = 0                 # 몇 개의 컴퓨터를 해킹 가능한가?
for n in range(1, N + 1):
    tmp = bfs(n)
    if tmp == cnt:
        ans.append(n)
    elif tmp > cnt:
        ans = [n]
        cnt = tmp

print(*ans)
