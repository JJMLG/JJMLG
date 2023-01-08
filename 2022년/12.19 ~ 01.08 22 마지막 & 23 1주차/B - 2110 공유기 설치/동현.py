import sys
from itertools import combinations
from pprint import pprint

k,c = map(int,input().split())
ls = []
for i in range(k):
    ls.append(int(input()))
ls.sort()
start = 1
end = 1000000001
result = 0
while start <= end:
    
    mid = (start + end) // 2

    cnt = 1

    left = 0 
    for i in range(1,k):
        if ls[i] - ls[left] >= mid:
            cnt += 1
            left = i
       

    if cnt >= c:
        start = mid +1 
        result = mid
        
    else:
        end = mid -1
        result = end
print(result)