from collections import deque
import sys
from itertools import combinations

arr = [list(input()) for _ in range(5)]

        
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def avail(comb):
    cnt = 0
    for x,y in comb:
        if arr[x][y] == 'S':
            cnt += 1
    if cnt >= 4:
        return True
    else:
        return False

def dfs(comb):
    visited = [False]*7
    queue = deque()
    queue.append(comb[0])
    visited[0] = True

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (nx, ny) in comb:
                nextIdx = comb.index((nx, ny))
                if not visited[nextIdx]:
                    queue.append((nx, ny))
                    visited[nextIdx] = True

    if False in visited:
        return False
    else:
        return True


pos = []
ans = 0
for i in range(5):
    for j in range(5):
        pos.append((i,j))

combs = list(combinations(pos,7))
for comb in combs:
    if avail(comb):
        if dfs(comb):
            ans += 1
print(ans)