import sys, itertools


n = int(input())
ls = list(map(int,input().split()))

maxx = 0
per = list(itertools.permutations(ls,n))
for j in range(len(per)):
    tmp = 0
    for i in range(n-1):
        tmp += abs(per[j][i]-per[j][i+1])

    if tmp >= maxx:
        maxx = tmp

print(maxx)