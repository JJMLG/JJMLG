from collections import deque
import sys

from itertools import combinations

n = int(input())
crane = list(map(int,input().split()))
crane.sort(reverse=True)
m = int(input())
box =  list(map(int,input().split()))
box.sort(reverse=True)
box = deque(box)

if box[0] > crane[0]:
    print(-1)
else:
  
    time = 0
    while box:
        flag = 0
        for i in crane:
            for j in box:
                if i >= j:
                    
                    box.remove(j)
                    break

        time +=1 
    print(time)
