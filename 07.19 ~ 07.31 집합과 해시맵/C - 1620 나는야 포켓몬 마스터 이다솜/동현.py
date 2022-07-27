import sys

dict = {}
dict_2 = {}
n,m = map(int,input().split())

for i in range(n):
    a = input()
    dict[a] = i+1
    dict_2[i+1] = a


for j in range(m):
    b = input()
    if b.isdigit() == True:
        print(dict_2[int(b)])
    else:
        print(dict[b])