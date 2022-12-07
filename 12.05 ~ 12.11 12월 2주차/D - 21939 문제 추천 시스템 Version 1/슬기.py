import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

n = int(input())
min_h = []
max_h = []
level = {}

for _ in range(n):
    p, l = map(int, input().split())
    heappush(min_h, (l, p))
    heappush(max_h, (-l, -p))
    if not level.get(p):
        level[p] = 0
    level[p] = l

m = int(input())

for _ in range(m):
    order = input().split()
    if order[0] == 'add':
        p, l = int(order[1]), int(order[2])
        heappush(min_h, (l, p))
        heappush(max_h, (-l, -p))
        if not level.get(p):
            level[p] = 0
        level[p] = l

    elif order[0] == 'solved':
        p = int(order[1])
        level[p] = 0
        # print(level)
    else:
        x = int(order[1])
        if x == 1:
            # print(level[-max_h[0][1]], -max_h[0][0], -max_h[0][1])
            while max_h and level[-max_h[0][1]] != -max_h[0][0]:
                # print(max_h)
                heappop(max_h)
            else:
                # print(max_h)
                print(-max_h[0][1])
        else:
            while min_h and level[min_h[0][1]] != min_h[0][0]:
                heappop(min_h)
            else:
                print(min_h[0][1])
