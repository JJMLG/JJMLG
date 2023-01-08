import sys

input = sys.stdin.readline

dict = {}
n,m = map(int,input().split())
for i in range(n):
    dict[input().rstrip()] = 1

tot = len(dict)
cnt = 0
for j in range(m):
    ls = input().rstrip().split(',')
    for k in ls:
        if k not in dict:
            continue
        if dict[k] == 1:
            dict[k] = 0
            cnt += 1
    
    print(tot-cnt)
    
'''
23분 40초
'''