import sys
from itertools import combinations
from pprint import pprint

k,n = map(int,input().split())
ls = []
for i in range(k):
    ls.append(int(input()))
start = 1
end = 2**31
result = 0
while start <= end:
    
    mid = (start + end) // 2
 
    t = 0

    for i in ls:
        t += i // mid
    
    if t >= n:
        start = mid + 1
        
    else:
        end = mid -1

print(end)