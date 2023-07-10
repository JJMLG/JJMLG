from collections import deque

def solution(maps):
    ans = []
    N, M = len(maps), len(maps[0])
    vis = [[0] * M for _ in range(N)]
    D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for r in range(N):
        for c in range(M):
            if maps[r][c] == 'X': continue
            if vis[r][c]: continue
            
            cnt = int(maps[r][c])
            vis[r][c] = 1
            Q = deque([(r, c)])
            while Q:
                i, j = Q.popleft()
                for d in D:
                    ni, nj = i + d[0], j + d[1]
                    if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
                    if maps[ni][nj] == 'X' or vis[ni][nj]: continue
                    vis[ni][nj] = 1
                    cnt += int(maps[ni][nj])
                    Q.append((ni,nj))
            ans.append(cnt)

    return sorted(ans) if ans else [-1]
