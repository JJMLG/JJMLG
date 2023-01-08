import sys

n = int(input())
ls = list(map(int,input().split()))

cnt = 0
maxx = 0
init = ls[0]
for i in range(1,n):

    if ls[i] < init:
        cnt +=1 
    else:
        init = ls[i]
        if cnt > maxx:
            maxx = cnt
        
        cnt = 0

if cnt >= maxx:
    print(cnt)
else:
    print(maxx)