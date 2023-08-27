import sys
import heapq


heap = []

n,h,t = map(int,input().split())
for _ in range(n):
    heapq.heappush(heap,int(input()))
max_heap = []
for item in heap:
    heapq.heappush(max_heap,(-item,item))


cnt = 0
for i in range(t):
    maxx = heapq.heappop(max_heap)[1]
    if maxx == 1:
        heapq.heappush(max_heap,(-1,1))

    elif maxx < h:
        heapq.heappush(max_heap,(-maxx,maxx))
    else:
        heapq.heappush(max_heap,(maxx//2*-1,maxx//2))
        cnt += 1
        
        

tot = heapq.heappop(max_heap)[1]
if tot > h:
    print('NO')
    print(tot)

else:
    print('YES')
    print(cnt)
    

