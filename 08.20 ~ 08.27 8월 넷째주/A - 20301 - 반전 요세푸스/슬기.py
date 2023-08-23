import sys
from collections import deque

sys.stdin = open('input.txt')

n, k, m = list(map(int, input().split()))

num = deque(range(1, n+1))
cnt = 0

while num:
    for i in range(k-1):
        t = num.popleft()
        num.append(t)
    print(num.popleft())
    cnt += 1
    if cnt == m:
        num = deque(reversed(num))
        cnt = 0


# ans = []
# pos = k - 1
# cnt = 0
# while num:
#     if cnt == m:
#         num = num[::-1]
#         pos = 0
#
#     if pos < len(num):
#         a = num.pop(pos)
#         cnt += 1
#         # print(num)
#         ans.append(a)
#         # print(a)
#         # visited[pos+1] = 1
#         pos += k - 1
#     elif pos >= len(num):
#         pos = pos - len(num)
#         # print(pos)
# # print(ans)
#
# for i in ans:
#     print(i)