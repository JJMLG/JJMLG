import sys
sys.stdin = open('input.txt')
from collections import deque

a, b = map(int, input().split())
q = deque([4, 7])
cnt = 0

while len(q) > 1:
    # t = q[0]
    t = q.popleft()

    if t <= b:
        if a <= t:
            cnt += 1
        q.append(t*10+4)
        q.append(t*10+7)
print(cnt)