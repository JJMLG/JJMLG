
import sys
import heapq
sys.stdin = open('input.txt')

n = int(input())
heap = []
for _ in range(n):
    heap.append(list(map(int, input().split())))
heap.sort(key=lambda x: x[0])


rooms = [heap[0][1]]
print(rooms)

for meeting in heap[1:]:
    if rooms[0] > meeting[0]:  # 회의실 회의 끝나는 시각이 대기중인 미팅 시각보다 늦으면
        heapq.heappush(rooms, meeting[1])
    else:
        heapq.heapreplace(rooms, meeting[1])

print(rooms)
print(len(rooms))