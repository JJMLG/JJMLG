import sys
sys.setrecursionlimit(99999)
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dist = [-1] * (N + 1)                       # 루트 노드에서의 거리
dist[1] = 0                                 # 1번이 루트

def recur(v):
    for nv in adj[v]:
        if dist[nv] < 0:
            dist[nv] = dist[v] + 1          # 지금에서 한칸 멀어짐
            recur(nv)

recur(1)                                    # 루트노드와 연결된 모든 점의 거리를 구한다

ans = 0
for i in range(2, N + 1):
    if len(adj[i]) == 1:                    # 부모가 1개란 의미 => 리프노드
        ans += dist[i]

print('Yes') if ans % 2 else print('No')    # 성원이가 먼저 -> 이기려면 말을 홀수번 움질이고 끝나야함


"""
리프에서 루트까지의 거리를 다 더하면 말을 몇 번 옮겨야 하는지 알 수 있다
sys.setrecursionlimit() 안에 들어가는 숫자가 메모리초과를 만들었다
10**6 했을 때는 메모리 초과였는데 99999 하니까 성공함
"""
