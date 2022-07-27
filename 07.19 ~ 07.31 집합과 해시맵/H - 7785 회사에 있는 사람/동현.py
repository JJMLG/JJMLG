import sys

n = int(input())
dict = {}
for i in range(n):
    a = input().split()
    if a[1] == 'enter':
        dict[a[0]] = 1
    else:
        dict[a[0]] -= 1


for k,v in sorted(dict.items(),reverse=True):
    if v == 1:
        print(k)