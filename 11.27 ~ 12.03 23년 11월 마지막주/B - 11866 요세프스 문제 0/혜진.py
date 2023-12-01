N, K = map(int, input().split())
circle = list(range(1, N+1))
i = 0
ans = ''
while circle:
    i = (i+K-1) % len(circle)
    ans += str(circle.pop(i)) + ', '
print(f'<{ans[:-2]}>')

###########################################################

from collections import deque

N, K = map(int, input().split())
Q = deque(list(range(1, N + 1)))

ans = ''
while Q:
    for _ in range(K - 1):
        Q.append(Q.popleft())
    ans += str(Q.popleft()) + ', '
print(f'<{ans[:-2]}>')
