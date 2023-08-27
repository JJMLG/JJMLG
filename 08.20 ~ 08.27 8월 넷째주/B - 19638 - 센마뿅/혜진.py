# 제일 큰 키가 맨 앞에 오도록 우선순위 큐 사용
# 최소 힙이기 때문에 -를 붙여서 사용

import sys, heapq
sys.stdin = open('input.txt')

N, H, T = map(int, input().split())
hq = [-int(input()) for _ in range(N)]
heapq.heapify(hq)

cnt = 0
for _ in range(T):
    if -hq[0] < H or hq[0] == -1:
        break
    new = (-heapq.heappop(hq)) // 2
    heapq.heappush(hq, -new)
    cnt += 1

tall = -heapq.heappop(hq)
if tall < H:
    print('YES')    # 가능하면
    print(cnt)      # 뿅망치 사용 횟수
else:
    print('NO')     # 불가능하면
    print(tall)     # 현재 가장 큰 거인의 키
