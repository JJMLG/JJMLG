import sys
sys.stdin = open('input.txt')

N, M, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    v, w = map(int, input().split())
    if v == w: continue             # 자기자신 제외
    adj[v].append(w)
    adj[w].append(v)
for i in range(N):
    adj[i] = list(set(adj[i]))      # 중복 제외

tot = 0                             # 총 비용
u = [0] * (N + 1)                   # 이미 친구인지 확인
for i in range(1, N + 1):
    if u[i]: continue
    u[i] = 1
    cost = A[i]
    Q = [i]
    while Q:
        v = Q.pop()
        for w in adj[v]:
            if u[w]: continue       # 이미 친구면 pass
            u[w] = 1                # 새 친구 사귐
            cost = min(cost, A[w])  # 최소 친구비 갱신
            Q.append(w)
    tot += cost                     # 친구비 지불
    if tot > k: break

if tot > k:  print('Oh no')         # 파산
else: print(tot)                    # 모두와 친구
