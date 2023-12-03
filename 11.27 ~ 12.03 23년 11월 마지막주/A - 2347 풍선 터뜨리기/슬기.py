from collections import deque
import sys
sys.stdin = open('input.txt')

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, val = q.popleft()
    ans.append(idx + 1)

    if val > 0:
        q.rotate(-(val - 1))
    elif val < 0:
        q.rotate(-val)

print(' '.join(map(str, ans)))