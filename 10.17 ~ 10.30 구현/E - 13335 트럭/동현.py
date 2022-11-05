import sys
from collections import deque

n,w,l = map(int,input().split())
ls = list(map(int,input().split()))

ans = 0
ls = deque(ls)
bridge = deque()

while True:
    
    if len(bridge) == 0 and len(ls) == 0:
        break

    for i in range(len(bridge)-1,-1,-1):
  
        bridge[i][1] += 1
        if bridge[i][1] > w:
            bridge.popleft()
    summ = 0
    for j in range(len(bridge)):
        summ += bridge[j][0]
    if ls and len(bridge) <= w and summ + ls[0] <= l:
        bridge.append([ls.popleft(),1])

    ans += 1

print(ans)