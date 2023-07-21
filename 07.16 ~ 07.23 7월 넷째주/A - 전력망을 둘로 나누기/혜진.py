# BFS
from collections import deque

def solution(n, wires):
    adj = [[] for _ in range(n + 1)]
    for a, b in wires:
        adj[a].append(b)
        adj[b].append(a)
    
    ans = n - 2                     # 1개와 나머지면 n - 2가 됨
    for a, b in wires:
        adj[a].remove(b)            # 연결 하나 끊고
        adj[b].remove(a)
        

        vis = [0] * (n + 1)         # 1번부터 BFS
        vis[1] = 1
        Q = deque([1])
        cnt = 1
        while Q:
            v = Q.popleft()
            for w in adj[v]:
                if not vis[w]:
                    vis[w] = 1
                    cnt += 1
                    Q.append(w)

        adj[a].append(b)            # 다시 연결
        adj[b].append(a)
        
        tmp = abs(n - cnt - cnt)    # 차이 절대값
        ans = min(tmp, ans)         # 갱신

    return ans
