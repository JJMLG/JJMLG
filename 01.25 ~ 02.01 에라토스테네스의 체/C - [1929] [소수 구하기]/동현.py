import sys

m, n = map(int,input().split())

ls = [0]*1000001
ls[1] = 1
ls[0] = 1
for i in range(2,1000001):
    if ls[i] == 1:
        continue

    cnt = 2
    while i*cnt <= 1000000:
        ls[i*cnt] = 1
        cnt += 1


for j in range(m,n+1):
    if ls[j] == 0:
        print(j)
