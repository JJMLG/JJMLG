import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')

n = int(input())
heap_max = []
heap_min = []
dict = {}
for i in range(n):
    p, l = map(int,input().split())
    heappush(heap_min, [l,p])
    heappush(heap_max, [-l,-p])
    if not dict.get(p):
        dict[p] = 0
    dict[p] = l

m = int(input())
for j in range(m):
    
    ls = input().split(' ')
    if ls[0] == 'add':
        ls[1] = int(ls[1])
        ls[2] = int(ls[2])
        heappush(heap_min,[ls[2],ls[1]])
        heappush(heap_max,[-ls[2],-ls[1]])
        if not dict.get(ls[1]):
            dict[ls[1]] = 0
        dict[ls[1]] = ls[2]

    elif ls[0] == 'recommend':
        if ls[1] == '1':
            while heap_max and dict[-heap_max[0][1]] != -heap_max[0][0]:
                heappop(heap_max)
            print(-heap_max[0][1])
        else:
            while heap_min and dict[heap_min[0][1]] != heap_min[0][0]:
                heappop(heap_min)
            print(heap_min[0][1])
    
    else:
        dict[int(ls[1])] = 0

