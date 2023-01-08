
import sys
import heapq

from collections import deque
from pprint import pprint

left = 0
right = (10**5) *20 +1
n,k = map(int,input().split())
ls = list(map(int,input().split()))
ans = 0
while left <= right:

    mid = (left+right) //2

    score = 0
    group = 0
    for i in ls:
        score += i
        if score >= mid:
            group += 1
            score = 0
    
    if group >= k:
        ans = mid
        left = mid + 1
    
    elif group < k:
        right = mid - 1

print(mid)