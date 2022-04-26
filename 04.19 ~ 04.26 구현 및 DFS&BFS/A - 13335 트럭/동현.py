from collections import deque
import sys

n, w, l = map(int,input().split())
ls = deque(map(int,input().split()))



# queue = [0,0]
cnt = 0
queue = deque([0]*w)
while ls:
    queue.popleft()
    weight = ls[0]
    if  sum(queue) + weight <= l and len(queue) < w :
        queue.append(ls.popleft())
    else:
        queue.append(0)
    cnt +=1

print(cnt+w)

