import sys

n = int(input())
dict = {}
ls = []
cnt = 0

for i in range(n):
    a = input()
    dict[a] = i+1

for j in range(n):
    a = input()
    ls.append(a)

for k in range(n):
    for t in range(k+1,n):
        if dict[ls[k]] > dict[ls[t]]:
            cnt +=1 
            break

print(cnt)