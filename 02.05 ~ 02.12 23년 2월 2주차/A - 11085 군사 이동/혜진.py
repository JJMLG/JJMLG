from heapq import heappush, heappop


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    pa = find(a)
    pb = find(b)

    if rank[pa] > rank[pb]:
        parent[pb] = pa
    else:
        parent[pa] = pb

        if rank[pa] == rank[pb]:
            rank[pb] += 1


N, E = map(int, input().split())
S, G = map(int, input().split())

Q = []
for _ in range(E):
    s, e, w = map(int, input().split())
    heappush(Q, (-w, s, e))

parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)

while Q:
    w, s, e = heappop(Q)

    union(s, e)
    if find(S) == find(G):
        print(-w)
        break


"""
1. 우선순위 큐로 길이 넓은 경로부터 연결한다
    -> heapq는 최소힙이니까 앞에 마이너스 해주기
2. 연결된 경로는 union을 통해 parent를 업데이트 한다
    -> 연결된 경로는 같은 부모를 갖는다
3. 만약 parent(S)와 parent(G)가 같은 값이 되면 방금 S와 G가 연결되었다는 의미이다
    -> 가장 최근 연결한 경로의 너비를 출력한다
"""
