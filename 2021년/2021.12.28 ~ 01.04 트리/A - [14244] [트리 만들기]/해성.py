import sys
n, m = map(int, input().split())

if m == 2:
    for i in range(n-1):
        print(i, i+1)
else:
    for i in range(n-m):
        print(i, i+1)
    for i in range(n-m+1, n):
        print(n-m, i)