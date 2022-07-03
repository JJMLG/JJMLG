import sys

n = int(input())
ls = []
for i in range(n):
    ls.append(list(input().split()))


ls.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in range(n):
    print(ls[i][0])