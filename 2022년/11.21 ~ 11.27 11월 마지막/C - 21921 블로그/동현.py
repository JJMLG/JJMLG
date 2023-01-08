import sys
from collections import deque

n,x = map(int,input().split())
ls = list(map(int,input().split()))

tmp = sum(ls[0:x])
maxx = tmp
cnt = 1
if sum(ls) == 0:
    print('SAD')
else:
    for i in range(1,n-x+1):
        tmp -= ls[i-1]
        tmp += ls[i+x-1]
        if maxx == tmp:
            cnt += 1
        if tmp > maxx:
            maxx = tmp
            cnt = 1
    print(maxx)
    print(cnt)