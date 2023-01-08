import sys


n = int(input())

ls = []
for i in range(n):
    a,b = map(int,input().split())
    ls.append([a,b])

winls = [0]*n
for j in range(n):
    win = 1
    for k in range(n):
        if j == k:
            continue
        if ls[j][0] < ls[k][0] and ls[j][1] < ls[k][1]:
            win += 1
    winls[j] = win

print(*winls)