INF = int(1e9)

N, M = map(int, input().split())
arr = [[INF]*N for _ in range(N)]
for m in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    if c < arr[a][b]:
        arr[a][b] = c

for k in range(N):
    for a in range(N):
        for b in range(N):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

for i in range(N):
    for j in range(N):
        if arr[i][j] == INF:
            if i != j:
                arr[i][j] = 0

result = INF
for i in range(N): result = min(result, arr[i][i])
print(result if result != INF else -1)