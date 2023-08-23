import sys, heapq
sys.stdin = open('input.txt')

n, h, t = list(map(int, input().split()))

height = []
for _ in range(n):
    a = int(input())
    heapq.heappush(height, (-a, a))
# print(height)

cnt = 0
for i in range(t):
    max_h = heapq.heappop(height)[1]
    if max_h < h:
        heapq.heappush(height, (-max_h, max_h))
        break
    elif max_h == 1:
        heapq.heappush(height, (-max_h, max_h))
    else:
        max_h = max_h // 2
        heapq.heappush(height, (-max_h, max_h))
        cnt += 1

if min(height)[1] < h:
    print('YES')
    print(cnt)
else:
    print('NO')
    print(heapq.heappop(height)[1])