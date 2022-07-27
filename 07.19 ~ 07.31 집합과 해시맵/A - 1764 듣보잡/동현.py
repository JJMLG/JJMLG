import sys


n,m = map(int,input().split())
dict = {}
ls = []
cnt = 0
for i in range(n):
    a = input()
    dict[a] = 1

for j in range(m):
    b = input()
    if b in dict:
        cnt +=1 
        ls.append(b)

print(cnt)
ls.sort()
for k in ls:
    print(k)