import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    road[n] = 1

    while q:
        t = q.popleft()
        if t == k:
            return road[t]

        if 0 <= t - 1 < 100001 and road[t-1] == 0:
            road[t-1] = road[t] + 1
            q.append(t-1)

        if 0 < t * 2 < 100001 and road[t*2] == 0:
            road[t*2] = road[t]
            q.append(t*2)

        if 0 <= t + 1 < 100001 and road[t+1] == 0:
            road[t+1] = road[t] + 1
            q.append(t+1)


n, k = map(int, input().split())
road = [0] * 100001

print(bfs(n))

