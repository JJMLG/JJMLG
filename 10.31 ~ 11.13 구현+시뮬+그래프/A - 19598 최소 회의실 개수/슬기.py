import sys, heapq
sys.stdin = open('input.txt')


n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
room.sort()

tmp = [0]
cnt = 1
for s, e in room:
    if s >= tmp[0]:
        heapq.heappop(tmp)
        # print(tmp,'111')
    else:
        cnt += 1
    heapq.heappush(tmp, e)
print(cnt)