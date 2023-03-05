'''
최소비용으로 간선을 연결하고
이미 갈 수 있는 노드이면 새로운 간선을 연결하지 않는다
연결된 간선의 수가 N - 2개가 되는 순간 두 그룹으로 나누어진 상태가 된다
'''
import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    if x > y:
        x, y = y, x
    parent[y] = x


N, M = map(int, input().split())
parent = [i for i in range(N)]

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a - 1, b - 1))
edges.sort()                        # 비용 기준으로 오름차순

ans = edgeCnt = 0
for c, a, b in edges:
    pa = find(a)
    pb = find(b)
    if pa != pb:                    # 아직 연결되지 않았으면
        union(pa, pb)               # 한 그룹으로 만든다
        ans += c                    # 유지해야하는 간선이니까 cost 추가
        edgeCnt += 1                # 연결한 간선의 수
        if edgeCnt == N - 2:
            break

print(ans)
