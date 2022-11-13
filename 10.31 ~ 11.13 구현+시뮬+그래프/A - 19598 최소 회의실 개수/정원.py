import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0]) # 회의 시작 시간 기준 오름차순 정렬
rooms = [0] # 비어있는 회의실 하나로 시작
result = 1 # 회의실은 한 개 이상 반드시 필요하다
for s, e in arr:
    if s >= rooms[0]: # 빈 회의실이 있다면
        heapq.heappop(rooms)
    else: # 빈 회의실이 없다면
        result += 1 # 최소 회의실 개수 추가
    heapq.heappush(rooms, e) # 회의를 시작하지
print(result)