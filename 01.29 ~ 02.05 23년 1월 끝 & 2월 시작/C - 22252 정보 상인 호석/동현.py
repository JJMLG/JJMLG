from collections import deque
import sys
import heapq
from itertools import combinations
from pprint import pprint

q = int(input())
dict = {}
ans = 0
for _ in range(q):
    inputs = list(input().split())
    # print(inputs)
    if inputs[1] not in dict.keys():
        dict[inputs[1]] = [] 

    if inputs[0] == '1':
        for j in range(int(inputs[2])):
            heapq.heappush(dict[inputs[1]],(-int(inputs[3+j]),int(inputs[3+j])))
    else:
        for j in range(int(inputs[2])):
            if dict[inputs[1]]:
                tmp = heapq.heappop(dict[inputs[1]])[1]
                ans += tmp
            else:
                break
    
    
print(ans)