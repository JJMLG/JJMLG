"""
모든 곳에서의 최단거리를 구한다 -> 플로이드 와샬
사이클 -> 출발점과 도착점이 같다 -> dist[i][i]
"""

V, E = map(int, input().split())

INF = 987654321
dist = [[INF] * V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = INF
for i in range(V):
    ans = min(ans, dist[i][i])

print(ans) if ans < INF else print(-1)
