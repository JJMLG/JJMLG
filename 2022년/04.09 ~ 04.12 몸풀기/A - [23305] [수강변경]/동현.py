import sys

ls = [0]*1000001
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt = 0
for i in range(n):
    ls[a[i]] += 1


for j in range(n):
    if ls[b[j]] > 0:
        ls[b[j]] -= 1

    else:
        cnt +=1 

print(cnt)