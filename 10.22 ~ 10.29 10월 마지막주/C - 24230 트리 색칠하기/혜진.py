from collections import deque

N = int(input())
color = [0] + list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

ans = 1 if color[1] else 0      # 1번 정점은 부모가 없으니 여기서 확인
visited = [False] * (N + 1)
Q = deque([1])
visited[1] = True
while Q:
    v = Q.popleft()
    for w in adj[v]:
        if visited[w]: continue
        visited[w] = True
        Q.append(w)
        if color[w] != color[v]:# w와 그 부모인 v를 비교해서
            ans += 1            # 색이 다르면 w에 색칠
print(ans)
